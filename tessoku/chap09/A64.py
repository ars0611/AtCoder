import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
#入力
n, m = map(int, input().split())
graph = [[] for _ in range(n)] #隣接リストで辺の情報を持つ
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].append((b, c)) #頂点aからbへの重みc
    graph[b].append((a, c)) #頂点bからaへの重みc

dist = [-1]*n #訪問済みの頂点であれば,そこまでの距離を持つ。未訪問なら-1
queue = []
heapq.heapify(queue) #ダイクストラ用のpriority queue
queue.append((0, 0))  # (距離, 頂点)
dist[0] = 0 #スタート地点の距離は0

#ダイクストラ法
while queue:
    cost_cur, pos_cur = heapq.heappop(queue)
    if dist[pos_cur] != -1 and dist[pos_cur] < cost_cur:
        continue  # 既に訪問済みで、より短い距離がある場合はスキップ
    dist[pos_cur] = cost_cur
    for pos_nxt, cost_nxt in graph[pos_cur]:
        if dist[pos_nxt] == -1:
            heapq.heappush(queue, (cost_cur + cost_nxt, pos_nxt))

for i in range(n):
    print(dist[i])

#costが小さいやつを優先してpopしたいので,タプルの形は(距離, 頂点)にする（一敗）