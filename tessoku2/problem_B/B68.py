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
p = list(map(int, input().split()))
ff = FordFulkerson(n + 2)
inf = 10 ** 18
for _ in range(m):
    a, b = map(int, input().split())
    ff.addEdge(a, b, inf)

ans = 0
for i in range(n):
    if p[i] >= 0:
        ans += p[i]
        ff.addEdge(0, i + 1, p[i])
        ff.addEdge(i + 1, n + 1, 0)
    else:
        ff.addEdge(0, i + 1, 0)
        ff.addEdge(i + 1, n + 1, - p[i])

minCut = ff.maxFlow(0, n + 1)
ans -= minCut
print(ans)
