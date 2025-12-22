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
# Ford-Fulkerson法による最大フローの求値
class FordFulkerson:
    # 初期化
    # 頂点数n, 隣接リストgraph, 到達フラグvisited
    def __init__(self, n):
        self.n = n
        self.graph = [[] for _ in range(n)]
        self.visited = [False] * n

    # グラフを構築
    # fr, to, cap = frからtoへの容量capのedge
    # graph[a] = [行先, 容量, 逆辺のindex]
    def addEdge(self, fr, to, cap):
        self.graph[fr].append([to, cap, len(self.graph[to])])
        self.graph[to].append([fr, 0, len(self.graph[fr]) - 1])

    # curからgoalまでのパスを深さ優先探索で探す
    # 容量が1以上かつ未訪問頂点に遷移し、flowが流せる場合、残余グラフの容量をflowだけ増減させる
    # パスが見つからなかった場合、0を返す
    def dfs(self, cur, goal, f):
        if cur == goal: 
            return f
        self.visited[cur] = True
        for edge in self.graph[cur]:
            to, cap, rev = edge
            if not self.visited[to] and cap > 0:
                flow = self.dfs(to, goal, min(f, cap))
                if flow:
                    edge[1] -= flow
                    self.graph[to][rev][1] += flow
                    return flow
        return 0

    # 頂点uからvまでの最大フローの総流量を返す
    def maxFlow(self, u, v):
        flow = 0
        f = inf =10 ** 9 + 7
        while f:
            self.visited = [False]*self.n
            f = self.dfs(u, v, inf)
            flow += f
        return flow

n, m = map(int, input().split())
c = [input().strip() for _ in range(n)]
ff = FordFulkerson(n + 24 + 2)
for i in range(n):
    ff.addEdge(0, i + 1, 10)
    for j in range(24):
        if not int(c[i][j]): continue
        ff.addEdge(i + 1, n + j + 1, 1)
for j in range(24):
    ff.addEdge(n + j + 1, n + 24 + 1, m)
maxFlow = ff.maxFlow(0, n + 24 + 1)
print("Yes" if maxFlow >= 24 * m else "No")

# ひとりにつき10時間働けるので、スタートから従業員まで容量10の辺
# n時につきm人働いてほしいので、時刻からtまで容量mの辺を張る
