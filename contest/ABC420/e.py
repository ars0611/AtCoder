import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
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

n, q = map(int, input().split())
c = [0]* n
p = [0]* n 
uf = UnionFind(n)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1 and not uf.same(query[1]-1, query[2]-1):
        w1 = p[uf.root(query[1]-1)]
        w2 = p[uf.root(query[2]-1)]
        uf.unite(query[1]-1, query[2]-1)
        p[uf.root(query[1]-1)] = w1 + w2
    elif query[0] == 2:
        if c[query[1]-1] == 0:
            c[query[1]-1] = 1
            p[uf.root(query[1]-1)] += 1
        else:
            c[query[1]-1] = 0
            p[uf.root(query[1]-1)] -= 1
    elif query[0] == 3:
        if p[uf.root(query[1]-1)] > 0:
            print("Yes")
        else:
            print("No")
