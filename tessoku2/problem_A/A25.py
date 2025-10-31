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
grid = [input().strip() for _ in range(h)]

dp = [[0] * w for _ in range(h)]
dp[0][0] = 1
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#": continue
        if j + 1 < w and grid[i][j + 1] == ".":
            dp[i][j + 1] += dp[i][j]
        if i + 1 < h and grid[i + 1][j] == ".":
            dp[i + 1][j] += dp[i][j]

print(dp[-1][-1])