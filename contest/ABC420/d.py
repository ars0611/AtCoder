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
grid = [list(input()) for _ in range(h)]
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            start = (i, j)
        elif grid[i][j] == "G":
            goal = (i, j)
visited = [[0] * w for _ in range(h)]
visited[start[0]][start[1]] = 1
queue = deque()
dist = 0
cnt = 0
queue.append((start[0], start[1], dist, cnt))
while queue:
    x, y, dist, cnt = queue.popleft()
    if visited[x][y] > 2:
        continue
    if (x, y) == goal:
        print(dist)
        exit()
    for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
        nx, ny = x + dx, y + dy
        if 0 <= nx < h and 0 <= ny < w and not (cnt % 2 == 0 and grid[nx][ny] == "x" or cnt % 2 == 1 and grid[nx][ny] == "o" or grid[nx][ny] == "#"):
            if grid[nx][ny] == "?":
                queue.append((nx, ny, dist + 1, cnt + 1))
            else:
                queue.append((nx, ny, dist + 1, cnt))

print(-1)

#TLEがとれねえよ。