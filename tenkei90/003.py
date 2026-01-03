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
n = int(input())
graph =[[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x:int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)
dist = [-1]*n
q = deque([(0, -1)])
while q:
    cur, prevd = q.popleft()
    if dist[cur] != -1: continue
    dist[cur] = prevd + 1
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            q.append((nxt, prevd + 1))
start = 0
for i in range(n):
    if dist[i] > dist[start]:
        start = i
dist2 = [-1]*n
q2 = deque([(start, -1)])
while q2:
    cur, prevd = q2.popleft()
    if dist2[cur] != -1: continue
    dist2[cur] = prevd + 1
    for nxt in graph[cur]:
        if dist2[nxt] == -1:
            q2.append((nxt, prevd + 1))
print(max(dist2) + 1)
