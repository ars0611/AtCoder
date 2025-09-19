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
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
q = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            sx, sy = i, j
            q.append((i, j, 0, 0)) # i, j, 次は縦移動, dist
            q.append((i, j, 1, 0)) # i, j, 次は横移動, dist
        if grid[i][j] == "G":
            gx, gy = i, j

ans = float('inf')
dy = [[0, 1], [0, -1]]
dx = [[1, 0], [-1, 0]]
visited = [set(), set()] #0:次縦, 1:次横
while q:
    x, y, direction, dist = q.popleft()
    if (x, y) in visited[direction]:
        continue
    if (x, y) == (gx, gy):
        ans = min(ans, dist)
    visited[direction].add((x, y))
    if direction == 0: #次は縦移動
        for ddx, ddy in dx:
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "#":
                q.append((nx, ny, 1, dist + 1))
    else: #次は横移動
        for ddx, ddy in dy:
            nx = x + ddx
            ny = y + ddy
            if 0 <= nx < h and 0 <= ny < w and grid[nx][ny] != "#":
                q.append((nx, ny, 0, dist + 1))
else:
    if ans == float('inf'):
        print(-1)
    else:
        print(ans)

# 縦横交互に移動が厄介
# 初手縦移動の世界と初手横移動の世界を分けてBFS
# すなわち頂点倍化