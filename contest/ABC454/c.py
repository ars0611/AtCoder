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
from functools import cmp_to_key
#----------------------------------------#
def dfs(curN, curD):
    if dist[curN] != 0:
        return
    dist[curN] = curD + 1
    for nxt in graph[curN]:
        if dist[nxt] == 0:
            dfs(nxt, curD + 1)
    return
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x:int(x) - 1, input().split())
    graph[a].append(b)
dist = [0]*n
dfs(0, 0)
cnt = 0
for d in dist:
    if d != 0:
        cnt += 1
print(cnt)
