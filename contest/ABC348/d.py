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
med = [[-1] * w for _ in range(h)] # 薬があればeを,なければ-1を格納
best = [[-1] * w for _ in range(h)] # マス(i,j)にいるときのエネルギーの最大値

n = int(input())
for _ in range(n):
    r, c, e = map(int, input().split())
    med[r - 1][c - 1] = e

queue = []
heapq.heapify(queue)
for i in range(h):
    for j in range(w):
        if grid[i][j] == "S":
            heapq.heappush(queue, (i, j, -med[i][j]))
            best[i][j] = max(best[i][j], med[i][j])
        if grid[i][j] == "T":
            gy = i
            gx = j

dx = [1, 0, -1, 0]
dy = [0, 1, 0, -1]
while queue:
    cury, curx, cure = heapq.heappop(queue)
    if cury == gy and curx == gx:
        print("Yes")
        break
    if best[cury][curx] != -cure or -cure <= 0:
        continue
    for k in range(4):
        ny = cury + dy[k]
        nx = curx + dx[k]
        if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] != "#":
            ne = max(-cure - 1, med[ny][nx])
            if ne > best[ny][nx]:
                best[ny][nx] = ne
                heapq.heappush(queue, (ny, nx, -ne))

else:
    print("No")