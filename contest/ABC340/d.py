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
n = int(input())
graph = [[] for _ in range(n)]
for i in range(n-1):
    a, b, x = map(int, input().split())
    x -= 1
    graph[i].append((a, i+1))
    graph[i].append((b, x))

visited = [False]*n
pq = graph[0][:]
heapq.heapify(pq)
visited[0] = True
while pq:
    cost, stage = heapq.heappop(pq)
    if visited[stage] == True:
        continue
    visited[stage] = True
    if stage == n - 1:
        print(cost)
        break
    for nxtcost, nxtstage in graph[stage]:
        if not visited[nxtstage]:
            heapq.heappush(pq, (cost+nxtcost, nxtstage))