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
    path.append(cur + 1)
    if cur == y - 1:
        print(*path)
        exit()
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)
    path.pop()
    return

n, x, y = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    u, v = map(lambda x:int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*n
path = []
dfs(x - 1)
