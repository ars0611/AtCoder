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
n, k = map(int, input().split())
a = list(map(int, input().split()))

ans = 0
i = 0
cur = 0
while i < n:
    if cur + a[i] <= k:
        cur += a[i]
        i += 1
    else:
        cur = 0
        ans += 1
if cur:
    ans += 1
print(ans)