import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
#入力
h, w, d = map(int, input().split())
grid = []
for i in range(h):
    s_i = list(input())
    grid.append(s_i)

#加湿器の置いてある座標をメモ
Humidifier = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == "H":
            Humidifier.append((i,j))

#多始点bfs
visited = [[False]*w for _ in range(h)]
queue = deque()
for h_i, h_j in Humidifier:
    visited[h_i][h_j] = True
    queue.append((h_i, h_j, 0)) #移動回数0

dx = [0, 1, 0, -1]
dy = [-1, 0, 1, 0]
while queue:
    i, j, dist = queue.popleft()
    if dist == d:
        continue
    for k in range(4):
        if 0 <= i+dy[k] <= h-1 and 0 <= j+dx[k]<= w-1 and not visited[i+dy[k]][j+dx[k]] and grid[i+dy[k]][j+dx[k]] != "#":
            visited[i+dy[k]][j+dx[k]] = True
            queue.append((i+dy[k], j+dx[k],dist+1))

ans = 0
for i in range(h):
    ans += visited[i].count(True)
print(ans)