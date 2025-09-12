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

dy = [1, 0, -1, 0]
dx = [0, 1, 0, -1]
for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            for k in range(4):
                ny = i + dy[k]
                nx = j + dx[k]
                if 0 <= ny < h and 0 <= nx < w and grid[ny][nx] == "#":
                    grid[i][j] = "@"
                    break

visited = [[False] * w for _ in range(h)]
ans = 1
queue = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "." and visited[i][j] == False:
            queue.append((i, j))
            visited[i][j] = True
            cnt = 1
            visited_at = set()

            while queue:
                cury, curx = queue.popleft()
                for k in range(4):
                    ny = cury + dy[k]
                    nx = curx + dx[k]
                    if 0 <= ny < h and 0 <= nx < w:
                        if not visited[ny][nx] and grid[ny][nx] == ".":
                            visited[ny][nx] = True
                            queue.append((ny, nx))
                            cnt += 1
                        elif grid[ny][nx] == "@":
                            if (ny, nx) not in visited_at:
                                cnt += 1
                                visited_at.add((ny, nx))
            ans = max(ans, cnt)
print(ans)