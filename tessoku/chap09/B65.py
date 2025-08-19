import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
# 入力
n, t = map(int, input().split())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append(b)
    graph[b].append(a)

#dfs!dfs!dfs!dfs!dfs!dfs!dfs!dfs!dfs!dfs!dfs!dfs!
visited = [False] * n
ans = [0] * n
def dfs(cur):
    visited[cur] = True
    for nxt in graph[cur]:
        if visited[nxt] == False:
            dfs(nxt)
            ans[cur] = max(ans[cur], ans[nxt] + 1)
dfs(t-1)
print(*ans)