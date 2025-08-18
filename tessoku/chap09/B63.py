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
r, c = map(int, input().split())
s_i, s_j = map(int, input().split())
g_i, g_j = map(int, input().split())
s_i -= 1; s_j -= 1; g_i -= 1; g_j -= 1
grid = []
for _ in range(r):
    grid.append(list(input()))

#初期化
for i in range(r):
    for j in range(c):
        if grid[i][j] == ".":
            grid[i][j] = -1
grid[s_i][s_j] = 0

#4方向探索する用の配列
dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]

#bfs
queue = deque()
queue.append((s_i, s_j))
while queue:
    cur_i, cur_j = queue.popleft()
    
    for d in range(4):
        nxt_i = cur_i + dx[d]
        nxt_j = cur_j + dy[d]
        
        if 0 <= nxt_i < r and 0 <= nxt_j < c and grid[nxt_i][nxt_j] == -1:
            grid[nxt_i][nxt_j] = grid[cur_i][cur_j] + 1
            queue.append((nxt_i, nxt_j))

print(grid[g_i][g_j])