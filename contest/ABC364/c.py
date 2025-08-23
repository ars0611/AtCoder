import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
d = []
for i in range(n):
    d.append((a[i], b[i]))

d.sort(key = lambda x: x[0], reverse=True)
cnt = 0
ans = n
for i in range(n):
    cnt += d[i][0]
    if cnt > x:
        ans = min(ans, i+1)
        break

d.sort(key = lambda x: x[1], reverse=True)
cnt = 0
for i in range(n):
    cnt += d[i][1]
    if cnt > y:
        ans = min(ans, i+1)
        break

print(ans)