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
    a, b = map(lambda x:int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)

dist = [-1]*n
q = deque([(0, 0)])
while q:
    curNode, curDist = q.popleft()
    if dist[curNode] != -1: continue
    dist[curNode] = curDist
    for nxtNode in graph[curNode]:
        if dist[nxtNode] == -1:
            q.append((nxtNode, curDist + 1))

for i in range(n):
    print(dist[i])
