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
move = [(-1, -1), (-1, 1), (1, 1), (1, -1)]
inf = 10**9
h, w = map(int, input().split())
grid = list(input().strip() for _ in range(h))

ans = [0]*min(h, w)
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            for k in range(4):
                ni = i + move[k][0]
                nj = j + move[k][1]
                if not(0 <= ni < h) or not(0 <= nj < w) or grid[ni][nj] != "#":
                    break
            else:
                size = inf
                for k in range(4):
                    curi = i
                    curj = j
                    streek = 0
                    while 0 <= curi < h and 0 <= curj < w and grid[curi][curj] == "#":
                        streek += 1
                        curi += move[k][0]
                        curj += move[k][1]
                    size = min(streek - 1, size)
                ans[size - 1] += 1

print(*ans)