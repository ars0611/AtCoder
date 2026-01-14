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
from functools import lru_cache
#----------------------------------------#
def dfs(cur):
    if visited[cur]: return
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
    return

n = int(input())
sx, sy, tx, ty = map(int, input().split())
circle = [tuple(map(int, input().split())) for _ in range(n)]
graph = [[] for _ in range(n)]
start = -1
goal = -1
for i in range(n):
    xi, yi, di = circle[i]
    if (sx - xi) ** 2 + (sy - yi) ** 2 == di ** 2:
        start = i
    if (tx - xi) ** 2 + (ty - yi) ** 2 == di ** 2:
        goal = i
    for j in range(i + 1, n):
        xj, yj, dj = circle[j]
        l = ((xi - xj) ** 2 + (yi - yj) ** 2)
        if abs(di - dj) ** 2 <= l <= (di + dj) ** 2:
            graph[i].append(j)
            graph[j].append(i) 
visited = [False]*n
dfs(start)
print("Yes" if visited[goal] else "No")
