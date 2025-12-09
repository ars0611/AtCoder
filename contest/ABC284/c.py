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
def dfs(cur):
    if visited[cur]: return
    visited[cur] = True
    for nxt in graph[cur]:
        if not visited[nxt]:
            dfs(nxt)

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x:int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

visited = [False]*n
ans = 0
for i in range(n):
    if not visited[i]:
        ans += 1
        dfs(i)

print(ans)
