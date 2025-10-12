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
n = int(input())
e = 1500
ans = 0
grid = [[0] * (e + 1) for _ in range(e + 1)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[a][d] -= 1
    grid[c][b] -= 1
    grid[c][d] += 1

for i in range(e + 1):
    for j in range(e):
        grid[i][j + 1] += grid[i][j]
for j in range(e + 1):
    for i in range(e):
        grid[i + 1][j] += grid[i][j]

ans = 0
for i in range(e + 1):
    for j in range(e + 1):
        if grid[i][j] > 0:
            ans += 1
print(ans)