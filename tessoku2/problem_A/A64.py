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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b, c = map(int, input().split())
    graph[a - 1].append((b - 1, c))
    graph[b - 1].append((a - 1, c))

dist = [-1]*n
priq = [(0, 0)]
heapq.heapify(priq)
while priq:
    curCost, curNode = heapq.heappop(priq)
    if dist[curNode] != -1: continue
    dist[curNode] = curCost
    for nxtNode, nxtCost in graph[curNode]:
        if dist[nxtNode] == -1:
            heapq.heappush(priq, (curCost + nxtCost, nxtNode))

for i in range(n):
    print(dist[i])
