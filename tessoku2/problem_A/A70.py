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
a = list(map(int, input().split()))
graph = [[] for _ in range(2 ** n)]
for _ in range(m):
    x, y, z = map(lambda x:int(x), input().split())
    for i in range(2 ** n):
        nxt = i ^ (1 << (n - x)) ^ (1 << (n - y)) ^ (1 << (n - z))
        graph[i].append(nxt)

init = 0
goal = 0
for i in range(n):
    if a[i]:
        init += 2 ** (n - i - 1)
    goal += 2 ** (n - i - 1)

dist = [-1] * (2 ** n)
q =  deque([(init, 0)])
while q:
    cur, d = q.popleft()
    if dist[cur] != -1: continue
    dist[cur] = d
    for nxt in graph[cur]:
        if dist[nxt] == -1:
            q.append((nxt, d + 1))
print(dist[goal])

# 実はグラフ
# 頂点をn個のランタンのonoffをビットで表したものとする
# 各頂点に各操作をしたときの状態が遷移先なので、そのように辺を張る
# 最初の状態から全てonの状態までの最短経路が答え
# グラフであることに気付くのは容易だが、何を頂点としてどう辺を張るかがポイント
