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
def dfs(cur, cost):
    if visited[cur][cost]: return
    visited[cur][cost] = True
    for nxt, weight in graph[cur]:
        if not visited[nxt][cost^weight]:
            dfs(nxt, cost^weight)
    return

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, w = map(int, input().split())
    graph[a - 1].append((b - 1, w))

visited = [[False]*(2**10) for _ in range(n)]
dfs(0,0)
for i in range(2**10):
    if visited[n - 1][i]:
        print(i)
        break
else:
    print(-1)