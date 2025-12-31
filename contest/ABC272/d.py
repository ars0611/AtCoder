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
graph = [[] for _ in range(n * n)]
move = []
for i in range(-n, n):
    for j in range(-n, n):
        if i ** 2 + j ** 2 != m: continue
        move.append((i, j))
for i in range(n):
    for j in range(n):
        for di, dj in move:
            ni = i + di
            nj = j + dj
            if 0 <= ni < n and 0 <= nj < n:
                graph[i * n + j].append(ni * n + nj)
dist = [[-1]*n for _ in range(n)]
q = deque([(0, 0, -1)])
while q:
    curi, curj, pred = q.popleft()
    if dist[curi][curj] != -1: continue
    dist[curi][curj] = pred + 1
    for nxt in graph[curi * n + curj]:
        nxti = nxt // n
        nxtj = nxt - nxt // n * n
        if dist[nxti][nxtj] == -1:
            q.append((nxti, nxtj, pred + 1))

for i in range(n):
    print(*dist[i] )

# i, jに対しk固定でl計算だとギリ間に合わない。
# 距離aqrt(m)となるような移動を列挙すれば十分高速、証明の仕方は知らない
