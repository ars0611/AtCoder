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
# 入力
n, m = map(int, input().split())

#(重み,移動先の頂点) <- heapqで使うから重みが先頭
node = [[] for _ in range(n)]
a = list(map(int, input().split()))
for _ in range(m):
    u, v, b = map(int, input().split())
    u -= 1
    v -= 1
    node[u].append((a[v] + b, v))
    node[v].append((a[u] + b, u))

# ダイクストラしちゃいます♪
queue = []
visited = [False] * n
dist = [float('inf')] * n
heapq.heapify(queue)
heapq.heappush(queue, (a[0], 0))
while queue:
    cur_cst, cur_pos = heapq.heappop(queue)
    if visited[cur_pos]:
        continue
    visited[cur_pos] = True
    dist[cur_pos] = cur_cst
    for nxt_cost, nxt_pos in node[cur_pos]:
        if not visited[nxt_pos]:
            heapq.heappush(queue, (cur_cst + nxt_cost, nxt_pos))

# 頂点1は別に出力しないでよし
print(*dist[1:])

# こういうのでいいんだよ

#配列が持つデータはboolとint混ぜると遅くなるから,visitedとdistで分けたほうが良い