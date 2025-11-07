import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]

di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
t = "snuke"
if grid[0][0] == "s":
    q = deque([(0, 0, 0)])
    visited = [[False]*w for _ in range(h)]
    while q:
        curi, curj, curcnt = q.popleft()
        if visited[curi][curj]: continue
        visited[curi][curj] = True
        for k in range(4):
            ni = curi + di[k]
            nj = curj + dj[k]
            ncnt = (curcnt + 1) % 5
            if 0 <= ni < h and 0 <= nj < w and grid[ni][nj] == t[ncnt]:
                q.append((ni, nj, ncnt))

    print("Yes" if visited[h - 1][w - 1] else "No")
else:
    print("No")