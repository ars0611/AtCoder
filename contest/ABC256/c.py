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
h1, h2, h3, w1, w2, w3 = map(int, input().split())
ans = 0
for i in range(1, 31):
    grid = [[0] * 3 for _ in range(3)]
    grid[0][0] = i
    for j in range(1, 31):
        grid[0][1] = j
        grid[0][2] = h1 - (i + j)
        for k in range(1, 31):
            grid[1][0] = k
            for l in range(1, 31):
                grid[1][1] = l
                grid[1][2] = h2 - (k + l)
                grid[2][0] = w1 - (i + k)
                grid[2][1] = w2 - (j + l)
                grid[2][2] = w3 - (grid[0][2] + grid[1][2])
                if all(grid[m][n] > 0 for m in range(3) for n in range(3)) and h3 == sum(grid[2]):
                    ans += 1
print(ans)
