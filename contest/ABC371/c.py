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
n = int(input())

#グラフg
#node_g[i][j] := 辺i-1とj-1を結ぶ辺があれば1,なければ0
m_g = int(input())
node_g = [[0]*n for _ in range(n)]
for i in range(m_g):
    u,v = map(int, input().split())
    node_g[u-1][v-1] = 1
    node_g[v-1][u-1] = 1

#グラフh
#node_hはnode_gと同様
m_h = int(input())
node_h = [[0]*n for _ in range(n)]
for i in range(m_h):
    u,v = map(int, input().split())
    node_h[u-1][v-1] = 1
    node_h[v-1][u-1] = 1

#value[i][j] := 頂点i-1のj-1に対する操作にかかる金額
#value[i][j] = value[j][i]なので,楽するために作っておく
value = [[0]*(n) for _ in range(n)]
for i in range(n-1):
    value_i = list(map(int, input().split()))
    for j, v in enumerate(value_i, start=i+1):
        value[i][j] = v
        value[j][i] = v

#このへんかなりだるい
#元のグラフgの頂点をほかの頂点に置き換えることを考える
#n <= 8　より順列全探索しても十分高速
ans = 10**18
idx = list(range(n))

for p in itertools.permutations(idx):
    cost = 0
    
    #頂点を置き換えるときのコストを計算
    for i in range(n):
        p_i = p[i]
        g_i = node_g[i]
        
        #置き換える前の頂点と置き換えた後の頂点p_iを見る
        #他の頂点それぞれに対し,xorで同じ辺があるか,どちらも辺がないか比較
        for j in range(i+1, n):
            if g_i[j] ^ node_h[p_i][p[j]]:
                cost += value[p_i][p[j]]

    ans = min(ans, cost)

print(ans)
#考察も実装もむずすぎる！