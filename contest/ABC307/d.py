import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations

#----------------------------------------#
n = int(input())
s = input().strip()

pre_sum = [0]
o = 0
c = 0
for i in range(n):
    if s[i] == "(":
        pre_sum.append(pre_sum[-1] + 1)
        o += 1
    elif s[i] == ")":
        pre_sum.append(pre_sum[-1] - 1)
        c += 1
    else:
        pre_sum.append(pre_sum[-1])

diff = o - c

l = 1
r = 1
todel = []
while l < n + 1:
    if s[l - 1] == "(" and pre_sum[l] >= diff:
        cnt = pre_sum[l - 1]
        r = l + 1
        while r < n + 1 and pre_sum[r] - cnt > 0:
            r += 1
        if r < n + 1 and pre_sum[r] == cnt and s[r - 1] == ")":
            todel.append((l - 1, r - 1))
            l = r + 1
        else:
            l += 1
    else:
        l += 1

cur = 0
ans = []
for l, r in todel:
    ans += s[cur:l]
    cur = r + 1
if cur < n:
    ans.append(s[cur:])

print("".join(ans))