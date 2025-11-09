import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
t = int(input())

mirr = {"A": 0, "B": 1, "C": 3}
di = [1, 0, -1, 0]
dj = [0, 1, 0, -1]

for _ in range(t):
    h, w = map(int, input().split())
    grid = [input().strip() for _ in range(h)]
    costs = [[[2 * 10 ** 5 + 1] * w for _ in range(h)] for _ in range(4)] # costs[dire][i][j]
    q = deque([(1, 0, 0, 0)]) # (dire, cost, i, j)
    
    while q:
        cur_dire, cur_cost, cur_i, cur_j = q.popleft()
        if costs[cur_dire][cur_i][cur_j] <= cur_cost: continue
        costs[cur_dire][cur_i][cur_j] = cur_cost
        
        for k in range(4):
            d = cur_dire ^ k
            if d == 2: continue
            nxt_i = cur_i + di[k]
            nxt_j = cur_j + dj[k]
            if not(0 <= nxt_i < h) or not(0 <= nxt_j < w): continue
            
            if d == mirr[grid[cur_i][cur_j]]:
                nxt_cost = cur_cost
                if costs[k][nxt_i][nxt_j] > nxt_cost:
                    q.appendleft((k, nxt_cost, nxt_i, nxt_j))
            
            else:
                nxt_cost = cur_cost + 1
                if costs[k][nxt_i][nxt_j] > nxt_cost:
                    q.append((k, nxt_cost, nxt_i, nxt_j))
    
    res = 2 * 10 ** 5 + 1
    for k in range(4):
        cost = costs[k][h - 1][w - 1]
        need = k ^ 1
        if need == 2: continue
        add = 0 if need == mirr[grid[h - 1][w - 1]] else 1
        res = min(res, cost + add)
    print(res)

# 向いている方向を状態に持ってマスを倍化
# XORで鏡の反射をやる <- これ天才要素
# 鏡の向きを変えるならコスト1,変えないならコスト0の二種のコストがある
# 01BFSで高速にやれる