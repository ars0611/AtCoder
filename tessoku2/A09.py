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
h, w, n = map(int, input().split())
grid = [[0]*(w + 1) for _ in range(h + 1)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    a -= 1
    b -= 1
    c -= 1
    d -= 1
    grid[a][b] += 1
    grid[a][d+1] -= 1
    grid[c+1][b] -= 1
    grid[c+1][d+1] += 1  

for i in range(h):
    for j in range(1,w):
        grid[i][j] += grid[i][j - 1]
for j in range(w):
    for i in range(1, h):
        grid[i][j] += grid[i - 1][j]

for i in range(h):
    print(*grid[i][:w])