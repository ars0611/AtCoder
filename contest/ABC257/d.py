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
pos = []
for _ in range(n):
    x, y, p = map(int, input().split())
    pos.append((x, y, p))
l = 0
r = 4 * 10 ** 9
while l < r:
    m = (l + r) // 2
    graph = [[] for _ in range(n)]
    for i in range(n - 1):
        xi, yi, pi = pos[i]
        for j in range(i + 1, n):
            xj, yj, pj = pos[j]
            d = abs(xi - xj) + abs(yi - yj)
            if pi * m >= d:
                graph[i].append(j)
            if pj * m >= d:
                graph[j].append(i)
    for i in range(n):
        visited = [False]*n
        q = deque([i])
        while q:
            cur = q.popleft()
            if visited[cur]: continue
            visited[cur] = True
            for nxt in graph[cur]:
                if not visited[nxt]:
                    q.append(nxt)
        if all(visited[j] for j in range(n)):
            r = m
            break
    else:
        l = m + 1
print(l)
