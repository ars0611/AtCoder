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
n = int(input())

d = defaultdict(int)
for i in range(n):
    ai, ci = map(int, input().split())
    if d[ci] == 0:
        d[ci] = ai
    else:
        d[ci] = min(d[ci], ai)

ans = 0
for v in d.values():
    ans = max(ans, v)

print(ans)