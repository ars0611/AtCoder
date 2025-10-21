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
ans = [grid[i][:] for i in range(h)]

direction = {0:"^", 1:"v", 2:">", 3:"<"}
q = deque()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "E":
            q.append((i, j, -1))

di = [-1, 1, 0, 0]
dj = [0, 0, 1, -1]
while q:
    curi, curj, d = q.popleft()
    if ans[curi][curj] != "." and ans[curi][curj] != "E": continue
    if ans[curi][curj] == ".":
        ans[curi][curj] = direction[d // 2 * 2 + (d + 1) % 2]
    for k in range(4):
        ni = curi + di[k]
        nj = curj + dj[k]
        if 0 <= ni < h and 0 <= nj < w and ans[ni][nj] == ".":
            q.append((ni, nj, k))

for i in range(h):
    s = ""
    for j in range(w):
        s += ans[i][j]
    print(s)