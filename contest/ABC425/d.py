import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]
newgrid = [[float('inf')] * w for _ in range(h)]
dx = [1, -1, 0, 0]
dy = [0, 0, 1, -1]
ans = 0
c = 1
q = deque()
visited = [[False] * w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            newgrid[i][j] = 0
            ans += 1
            for k in range(4):
                ni = i + dx[k]
                nj = j + dy[k]
                if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == "." and not visited[ni][nj]:
                    visited[ni][nj] = True
                    q.append((ni, nj, c))

while q:
    x, y, c = q.popleft()
    cnt = 0
    for k in range(4):
        nx = x + dx[k]
        ny = y + dy[k]
        if 0 <= nx < h and 0 <= ny < w and newgrid[nx][ny] < c:
            cnt += 1
    if cnt == 1:
        ans += 1
        newgrid[x][y] = c
        for k in range(4):
            nx = x + dx[k]
            ny = y + dy[k]
            if 0 <= nx < h and 0 <= ny < w and newgrid[nx][ny] == float('inf') and not visited[nx][ny]:
                visited[nx][ny] = True
                q.append((nx, ny, c + 1))
print(ans)