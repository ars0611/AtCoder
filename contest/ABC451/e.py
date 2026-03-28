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
from functools import cmp_to_key
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

n = int(input())
uf = UnionFind(n)
a = [list(map(int, input().split())) for _ in range(n - 1)]
graph = [[] for _ in range(n)]
p = defaultdict(list)
for i in range(n):
    for j in range(n - i - 1):
        p[a[i][j]].append((i, i + j + 1))
for pp in range(1, 10000):
    for s, g in p[pp]:
        if uf.same(s, g):
            continue
        uf.unite(s, g)
        graph[s].append(g)
        graph[g].append(s)

# MSTして最後にaとの整合性の確認をしたい。後で解く
