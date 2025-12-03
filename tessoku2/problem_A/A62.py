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
        dfs(nxt)
    return

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x:int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)
visited = [False]*n
dfs(0)
print("The graph is connected." if all(visited) else "The graph is not connected.")
