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
grid = [[0] * 101 for _ in range(101)]
for _ in range(n):
    a, b, c, d = map(int, input().split())
    for i in range(c, d):
        for j in range(a, b):
            grid[i][j] += 1

s = 0
for i in range(101):
    for j in range(101):
        if grid[i][j] > 0:
            s += 1
print(s)