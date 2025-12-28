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
def dfs(cur, prev):
    dist[cur] = dist[prev] + 1
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            dfs(nxt, cur)

n = int(input())
a = list(map(int, input().split()))
graph =[[] for _ in range(2 * n + 1)]
for i in range(n):
    graph[a[i] - 1].append(2 * (i + 1) - 1)
    graph[a[i] - 1].append(2 * (i + 1))
dist = [-1] * (2 * n + 1)
dist[0] = -1
dfs(0, 0)
for d in dist:
    print(d)
