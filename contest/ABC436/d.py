import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
inf = 10**9
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
warp = defaultdict(list)
for i in range(h):
    for j in range(w):
        if grid[i][j] != "." and grid[i][j] != "#":
            warp[grid[i][j]].append((i, j))

q = deque([(0, 0, 0)])
dist = [[inf]*w for _ in range(h)]
used = set()
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
while q:
    curi, curj, curc = q.popleft()
    if curc >= dist[curi][curj]: continue
    dist[curi][curj] = curc
    if grid[curi][curj] != "." and grid[curi][curj] not in used:
        for nxti, nxtj in warp[grid[curi][curj]]:
            q.append((nxti, nxtj, curc + 1))
        used.add(grid[curi][curj])
    for k in range(4):
        nxti = curi + di[k]
        nxtj = curj + dj[k]
        if 0 <= nxti < h and 0 <= nxtj < w and curc + 1 < dist[nxti][nxtj] and grid[nxti][nxtj] != "#":
            q.append((nxti, nxtj, curc + 1))
print(dist[h - 1][w - 1] if dist[h - 1][w - 1] != inf else -1)
