import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
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
s = input().strip()
n = len(s)
l = 0
r = 0
ans = 0
while l < n:
    r = l
    while r < n and s[l] == s[r]:
        r += 1
    if r < n and int(s[r]) == int(s[l]) + 1:
        d = r
        while r < n and s[d] == s[r]:
            r += 1
        ans += min(d - l, r - d)
        l = d
    else:
        l = r

print(ans)