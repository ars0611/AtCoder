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
def bfs(node):
    isBipartite = True
    q = deque([(node, -1)])
    white = 0
    black = 0
    while q:
        cur, prevColor = q.popleft()
        if color[cur] != 0: continue
        color[cur] = -1 * prevColor
        if color[cur] == 1:
            white += 1
        else:
            black += 1
        for nxt in graph[cur]:
            if color[nxt] == color[cur]:
                isBipartite = False
            elif color[nxt] == 0:
                q.append((nxt, color[cur]))
    return white, black, isBipartite
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x: int(x) - 1, input().split())
    graph[u].append(v)
    graph[v].append(u)

color = [0]*n
isBipartite = True
ans = n * (n - 1) // 2 - m
for i in range(n):
    if color[i] != 0: continue
    white, black, isBipartite = bfs(i)
    if not isBipartite:
        ans = 0
        break
    ans -= black * (black - 1) // 2 + white * (white - 1) // 2
print(ans)
