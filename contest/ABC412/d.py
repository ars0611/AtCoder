import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
graph = [[0] * n for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x: int(x) - 1, input().split())
    graph[a][b] = graph[b][a] = 1

edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
ans = 10**9
for e in itertools.combinations(edges, n):
    deg = [0] * n
    for u, v in e:
        deg[u] += 1
        deg[v] += 1
    if all(d == 2 for d in deg):
        ans = min(ans, n + m - 2 * sum(graph[u][v] for u, v in e))

print(ans)

# 隣接行列で辺を管理したほうが楽
# すべての頂点の次数が2となるときの辺の数はn
# edgesで全辺を列挙し、そこからn本選び取る全探索
# すべての頂点の次数が2のとき、操作回数を求めて答えを更新
# 包除原理で操作回数を求める。元の辺 と 今の辺 の和集合取って、今の辺 かつ 元の辺 を減算