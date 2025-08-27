import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, t = map(int, input().split())
s = input()
x = list(map(int, input().split()))

pos_x = []
neg_x = []
for i in range(n):
    if s[i] == "1":
        pos_x.append(x[i])
    else:
        neg_x.append(x[i])
ans = 0
neg_x.sort()
for i, pos_x_i in enumerate(pos_x):
    idx_before = bisect.bisect_left(neg_x, pos_x_i)
    idx_after = bisect.bisect_left(neg_x, pos_x_i + 2 * t)
    if idx_after < len(neg_x) and neg_x[idx_after] == pos_x_i + 2 * t:
        ans += 1
    ans += idx_after - idx_before
print(ans)