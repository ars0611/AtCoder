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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    graph[u].append((v, w))
    graph[v].append((u, w))

ans = float("inf")
visited = [False] * n
def dfs(cur, cost):
    global ans
    visited[cur] = True
    if cur == n - 1:
        ans = min(ans, cost)
    for nxt, nxtcost in graph[cur]:
        if not visited[nxt]:
            dfs(nxt, cost ^ nxtcost)
    visited[cur] = False # 遡るときに非訪問済みにするのがミソ

dfs(0,0)
print(ans)