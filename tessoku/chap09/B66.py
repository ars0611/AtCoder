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

#入力
n, m = map(int, input().split())
load = []
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    load.append((a, b))

#辺を削除するのは難しいのでqueryを逆順に取得することで,辺を順に統合していくと見て処理
#順でクエリを取得した際に削除しなかった辺はもともと統合されているので注意
q = int(input())
uf = UnionFind(n)
query = []
for _ in range(q):
    query_i = list(map(int, input().split()))
    query.append(query_i)

#削除される路線を列挙
deleted = set()
for query_i in query:
    if query_i[0] == 1:
        x = query_i[1] - 1
        deleted.add(x)

#先に統合しておく
for i in range(m):
    if i not in deleted:
        uf.unite(load[i][0], load[i][1])
query.reverse()
ans = []
for query_i in query:
    if query_i[0] == 1:
        x = query_i[1] - 1
        uf.unite(load[x][0], load[x][1])
    else:
        u = query_i[1] - 1
        v = query_i[2] - 1
        if uf.same(u, v):
            ans.append("Yes")
        else:
            ans.append("No")

for a in reversed(ans):
    print(a)