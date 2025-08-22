import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, m = map(int, input().split())
a = list(map(int, input().split()))

if sum(a) <= m:
    print("infinite")
    exit()

l = 0
r = m
while l < r:
    mid = (l + r) // 2
    s = 0
    for i in range(n):
        s += min(a[i], mid)
    if s <= m:
        l = mid + 1
    else:
        r = mid
print(r-1)