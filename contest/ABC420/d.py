import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
h, w = map(int, input().split())
grid_0 = [list(input()) for _ in range(h)] #スイッチを押した回数が偶数回の世界
grid_1 = [grid_0[i][:] for i in range(h)] #スイッチを押した回数が奇数回の世界

for i in range(h):
    for j in range(w):
        if grid_0[i][j] == "S":
            start = (i,j)
        if grid_0[i][j] == "G":
            goal = (i,j)
        if grid_0[i][j] == "o":
            grid_1[i][j] = "x"
        if grid_0[i][j] == "x":
            grid_1[i][j] = "o"

visited_0 = [[False] * w for _ in range(h)]
visited_1 = [[False] * w for _ in range(h)]
dist_0 = [[10 ** 18] * w for _ in range(h)]
dist_1 = [[10 ** 18] * w for _ in range(h)]
cnt = 0
cost = 0
queue = deque()
queue.append((cost, start[0], start[1], cnt))
while queue:
    cost, x, y, cnt = queue.popleft()
    if cnt % 2 == 0 and visited_0[x][y] or cnt % 2 == 1 and visited_1[x][y]:
        continue
    if cnt % 2 == 0:
        visited_0[x][y] = True
        dist_0[x][y] = cost
    else:
        visited_1[x][y] = True
        dist_1[x][y] = cost
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w:
            if cnt % 2 == 0:
                if grid_0[nx][ny] == "?":
                    queue.append((cost + 1, nx, ny, cnt + 1))
                elif grid_0[nx][ny] != "#" and grid_0[nx][ny] != "x":
                    queue.append((cost + 1, nx, ny, cnt))
            else:
                if grid_1[nx][ny] == "?":
                    queue.append((cost + 1, nx, ny, cnt + 1))
                elif grid_1[nx][ny] != "#" and grid_1[nx][ny] != "x":
                    queue.append((cost + 1, nx, ny, cnt))
ans = min(dist_0[goal[0]][goal[1]], dist_1[goal[0]][goal[1]])
if ans == 10 ** 18:
    print(-1)
else:
    print(ans)

#頂点倍化初耳upsolve