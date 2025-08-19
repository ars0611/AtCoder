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
n, k = map(int, input().split())
graph = [set() for _ in range(n)]

for _ in range(n-1):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    graph[a].add(b)
    graph[b].add(a)
v = list(map(int, input().split()))
v = [x-1 for x in v]
v = set(v)

#ある頂点について,それが持つ辺の数,すなわち次数が1で,かつその辺の先がvに含まれない場合,その頂点は削除してよい
deg = [len(graph[i]) for i in range(n)] #各頂点の次数
q = [i for i, deg_i in enumerate(deg) if deg_i == 1] #次数が1の頂点
ans = n
for p in q:
    
    #l29より, pがvに含まれない場合, pの隣接頂点を削除する
    if p in v:
        continue
    
    #頂点を削除する
    pp = graph[p].pop()
    graph[pp].remove(p)
    ans -= 1

    #削除後の頂点ppの次数が1になった場合, qに追加する
    if len(graph[pp]) == 1:
        q.append(pp)

print(ans)