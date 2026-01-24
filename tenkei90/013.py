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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

heap = []
heapq.heapify(heap)
heapq.heappush(heap, (0, 0)) # 時間, 街
dist = [-1] * n # 街1からkまでの最短時間
while heap:
    curTime, curNode = heapq.heappop(heap)
    if dist[curNode] != -1: continue
    dist[curNode] = curTime
    for nxtNode, time in graph[curNode]:
        if dist[nxtNode] == -1:
            heapq.heappush(heap, (curTime + time, nxtNode))
hheap = []
heapq.heapify(hheap)
heapq.heappush(hheap, (0, n - 1)) # 時間, 街
ddist = [-1] * n # 街1からkまでの最短時間
while hheap:
    curTime, curNode = heapq.heappop(hheap)
    if ddist[curNode] != -1: continue
    ddist[curNode] = curTime
    for nxtNode, time in graph[curNode]:
        if ddist[nxtNode] == -1:
            heapq.heappush(hheap, (curTime + time, nxtNode))

for i in range(n):
    print(dist[i] + ddist[i])

# ダイクストラ両端からするだけ
# 街1から街kまでの最短経路と街nから街kまでの最短経路を求めることで街kを経由した街1から街nまでの最短経路が求まる
