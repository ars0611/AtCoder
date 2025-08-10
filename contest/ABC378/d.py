import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
#入力
h, w, k = map(int, input().split())
grid = []
for i in range(h):
    s_i = list(input())
    grid.append(s_i)

ans = 0
#dfs定義
visited = [[False]*w for _ in range(h)]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
def dfs(i, j, cnt, k):
    
    global ans
    if cnt == k:
        ans += 1
        return
    
    visited[i][j] = True
    for l in range(4):
        nx = j + dx[l]
        ny = i + dy[l]
        if 0 <= nx <= w-1 and 0 <= ny <= h-1 and visited[ny][nx] == False and grid[ny][nx] == ".":
            dfs(ny, nx, cnt+1, k)
    visited[i][j] = False

ans = 0
for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            dfs(i, j, 0, k)

print(ans)