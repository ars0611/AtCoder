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
edge = 1500
grid = [[0]*edge for _ in range(edge)]
for _ in range(n):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    grid[x][y] += 1

s = [[0]*(edge+1) for _ in range(edge+1)]
for i in range(edge):
    for j in range(edge):
        s[i+1][j+1] += s[i+1][j] + grid[i][j]
for j in range(edge):
    for i in range(edge):
        s[i+1][j+1] += s[i][j+1]

q = int(input())
for _ in range(q):
    a, b, c, d = map(int, input().split())
    print(s[c][d] - s[c][b-1] - s[a-1][d] + s[a-1][b-1])