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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
deg = [0]*n
for _ in range(m):
    u, v = map(lambda x:int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)
    deg[u] += 1
    deg[v] += 1

edge = set()
start = -1
ans = True
for i in range(n):
    if deg[i] == 1:
        if not edge:
            start = i
        edge.add(i)
    elif deg[i] > 2:
        ans = False
if start == -1 or len(edge) != 2:
    ans = False
if ans:
    visited = [False]*n
    cur = start
    while not visited[cur]:
        visited[cur] = True
        for nxt in graph[cur]:
            if not visited[nxt]:
                cur = nxt
    if not all(visited):
        ans = False
print("Yes" if ans else "No")
