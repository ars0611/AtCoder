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
# Union-Find木
class UnionFind:
    # n頂点のUnion-Find木を生やす
    # 親を表す配列とグループのサイズを表す配列を用意する
    def __init__(self, n):
        self.par = [-1] * n
        self.siz = [1] * n
    
    # 頂点xの根を求める関数を定義する
    def root(self, x):
        # 根にたどり着くまで親をたどる
        while self.par[x] != -1:
            x = self.par[x]
        return x
    
    # 頂点u,vを統合する関数を定義する
    def unite(self, u, v):
        root_u = self.root(u)
        root_v = self.root(v)
        
        # 既に統合されているなら何もしない
        if root_u == root_v:
            return

        # 頂点数の多い方に統合する（これにより計算量が抑えられる）
        if self.siz[root_u] < self.siz[root_v]:
            self.par[root_u] = root_v
            self.siz[root_v] += self.siz[root_u]
        else:
            self.par[root_v] = root_u
            self.siz[root_u] += self.siz[root_v]

    # 頂点u,vが同じグループに属するか判定する関数を定義する
    def same(self, u, v):
        return self.root(u) == self.root(v)

h, w = map(int, input().split())
red = set()
dr = [-1, 0, 1, 0]
dc = [0, 1, 0, -1]
uf = UnionFind(h * w)
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        r = query[1] - 1
        c = query[2] - 1
        node = r * w + c
        for k in range(4):
            nr = r + dr[k]
            nc = c + dc[k]
            nnode = (r + dr[k]) * w + c + dc[k]
            if nnode in red and 0 <= nr < h and 0 <= nc < w:
                uf.unite(node, nnode)
        red.add(node)
    else:
        ra = query[1] - 1
        ca = query[2] - 1
        rb = query[3] - 1
        cb = query[4] - 1
        nodea = ra * w + ca
        nodeb = rb * w + cb
        print("Yes" if uf.same(nodea, nodeb) and nodea in red and nodeb in red else "No")

# 上下左右を通って移動する操作は毎回dfs/bfsするのは遅いのでunionFindで同じ木かどうか判定することで高速に行える
# 赤に塗ったマスをsetで持ち、塗る際に周囲4方向に赤マスがあれば木をマージ
# 
