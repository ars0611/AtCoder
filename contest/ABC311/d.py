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
n, m = map(int, input().split())
grid = [input().strip() for _ in range(n)]

rows = [[] for _ in range(n)]
cols = [[] for _ in range(m)]
g = [[""]*m for _ in range(n)]
for i in range(n):
    for j in range(m):
        if grid[i][j] == "#":
            rows[i].append(j)
            cols[j].append(i)
        g[i][j] = grid[i][j]

q = deque([(1, 1)])
visited = set()
while q:
    curi, curj = q.popleft()
    if (curi, curj) in visited: continue
    visited.add((curi, curj))
    g[curi][curj] = "o"
    
    x = bisect.bisect_left(rows[curi], curj)
    y = bisect.bisect_left(cols[curj], curi)
    left = rows[curi][x - 1] + 1
    right = rows[curi][x] - 1
    up = cols[curj][y] - 1
    down = cols[curj][y - 1] + 1
    for k in range(left, right + 1):
        g[curi][k] = "o"
    for k in range(down , up + 1):
        g[k][curj] = "o"
    
    if (curi, left) not in visited: q.append((curi, left))
    if (curi, right) not in visited: q.append((curi, right))
    if (up, curj) not in visited: q.append((up, curj))
    if (down, curj) not in visited: q.append((down, curj))

ans = 0
for i in range(n):
    for j in range(m):
        if g[i][j] == "o":
            ans += 1
print(ans)