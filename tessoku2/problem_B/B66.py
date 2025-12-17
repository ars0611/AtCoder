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
uf = UnionFind(n)
route = [tuple(map(lambda x:int(x) - 1, input().split())) for _ in range(m)]
q = int(input())
isNotSafe = set()
queries = []
for i in range(q):
    query = list(map(int, input().split()))
    queries.append(query)
    if query[0] == 1:
        isNotSafe.add(query[1] - 1)
for i in range(m):
    if i in isNotSafe: continue
    uf.unite(route[i][0], route[i][1])
ans = []
for i in range(q - 1, -1, -1):
    query = queries[i]
    if query[0] == 1:
        uf.unite(route[query[1] - 1][0], route[query[1] - 1][1])
    else:
        ans.append("Yes" if uf.same(query[1] - 1, query[2] - 1) else "No")
ans.reverse()
print("\n".join(ans))
