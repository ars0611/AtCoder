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

par = [-1]*n
heap = [(0, 0, 0)]
heapq.heapify(heap)
while heap:
    curCost, curNode, prevNode = heapq.heappop(heap)
    if par[curNode] != -1: continue
    par[curNode] = prevNode
    for nxtNode, nxtCost in graph[curNode]:
        if par[nxtNode] == -1:
            heapq.heappush(heap, (curCost + nxtCost, nxtNode, curNode))

revPath = []
cur = n - 1
while cur != 0:
    revPath.append(cur)
    cur = par[cur]
path = [0] + list(reversed(revPath))
path = [node + 1 for node in path]
print(*path)
