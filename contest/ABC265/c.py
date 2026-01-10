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
from functools import lru_cache
#----------------------------------------#
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
d = {"U":(-1, 0), "D":(1, 0), "L":(0, -1), "R":(0, 1)}
curi = 0
curj = 0
visited = [[False]*w for _ in range(h)]
for _ in range(h * w):
    visited[curi][curj] = True
    ni = curi + d[grid[curi][curj]][0]
    nj = curj + d[grid[curi][curj]][1]
    if 0 <= ni < h and 0 <= nj < w and not visited[ni][nj]:
        curi = ni
        curj = nj
    elif 0 <= ni < h and 0 <= nj < w:
        print(-1)
        break
    else:
        print(curi + 1, curj + 1)
        break
else:
    print(curi + 1, curj)
