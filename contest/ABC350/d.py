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
    
n, m = map(int, input().split())
g = [[] for _ in range(n)]
uf = UnionFind(n)
for _ in range(m):
    a, b = map(int, input().split())
    g[a - 1].append(b - 1)
    uf.unite(a - 1, b - 1)

path = defaultdict(int)
for i in range(n):
    pi = uf.root(i)
    path[pi] += len(g[i])

ans = 0
for k, v in path.items():
    size = uf.siz[k]
    ans += size * (size - 1) // 2 - v
print(ans)