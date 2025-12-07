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
r, c = map(int, input().split())
sy, sx = map(lambda x:int(x) - 1, input().split())
gy, gx = map(lambda x:int(x) - 1, input().split())
grid = [input().strip() for _ in range(r)]

dy = [-1, 0, 1, 0]
dx = [0, 1, 0, -1]
dist = [[-1]*c for _ in range(r)]
q = deque([(sy, sx, 0)])
while q:
    cury, curx, curd = q.popleft()
    if dist[cury][curx] != -1: continue
    dist[cury][curx] = curd
    for k in range(4):
        nxty = cury + dy[k]
        nxtx = curx + dx[k]
        if 0 <= nxty < r and 0 <= nxtx < c and grid[nxty][nxtx] == "." and dist[nxty][nxtx] == -1:
            q.append((nxty, nxtx, curd + 1))
print(dist[gy][gx])
