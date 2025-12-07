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
def dfs(curNode, curDist):
    if dist[curNode] != -1: return
    dist[curNode] = curDist
    for nxtNode in graph[curNode]:
        if dist[nxtNode] == -1:
            dfs(nxtNode, curDist + 1)

n, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x:int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1]*n
dfs(t - 1, 0)
depth = [[] for _ in range(n)]
for i in range(n):
    depth[dist[i]].append(i)

rank = defaultdict(int)
seen = [False]*n
for i in range(n):
    for j in depth[- i - 1]:
        seen[j] = True
        for k in graph[j]:
            if seen[k]: continue
            rank[k] = max(rank[k], rank[j] + 1)

ans = [0]*n
for k, v in rank.items():
    ans[k] = v
print(*ans)
