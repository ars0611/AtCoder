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
n, m = map(int, input().split())
node = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    a -= 1
    b -= 1
    node[a].append(b)
    node[b].append(a)


dist = [-1] * n #頂点1から各頂点までの距離を持つ
queue = deque() #bfs用のqueue
queue.append(0) #スタート地点をqueueに追加
dist[0] = 0 #スタート地点の距離は0

#bfs
while queue:
    
    cur = queue.popleft()
    
    for nxt in node[cur]:
        if dist[nxt] == -1:
            queue.append(nxt)
            dist[nxt] = dist[cur] + 1

for d in dist:
    print(d)

#わざわざvisitedとか用意せずともdistだけで訪れたかどうか管理できる