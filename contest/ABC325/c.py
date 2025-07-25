import sys
sys.setrecursionlimit(10**6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
#入力
h, w = map(int, input().split())
grid = [["."]*w for _ in range(h)]
for i in range(h):
    s = input()
    for j in range(w):
        if s[j] == "#":
            grid[i][j] = "#"

#八方向探索しながらdfs
#dx,dyは八方向探索用
dy = [-1, -1, -1, 0, 0, 1, 1, 1]
dx = [-1, 0, 1, -1, 1, -1, 0, 1]
visited = [[False]*w for _ in range(h)]
def dfs(i,j):
    visited[i][j] = True
    for d in range(8):
        ny = i + dy[d]
        nx = j + dx[d]
        if 0 <= nx < w and 0 <= ny < h and not visited[ny][nx] and grid[ny][nx] == "#":
            dfs(ny,nx)

#連結成分を数えあげる
ans = 0
for i in range(h):
    for j in range(w):
        if not visited[i][j] and grid[i][j] == "#":
            dfs(i,j)
            ans += 1

print(ans)
