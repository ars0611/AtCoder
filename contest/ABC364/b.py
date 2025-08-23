import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
h, w = map(int, input().split())
cur_i, cur_j = map(int, input().split())
cur_i -= 1
cur_j -= 1
grid = [list(input()) for _ in range(h)]
x = input()
for c in x:
    if c == "L":
        if cur_j - 1 >= 0 and grid[cur_i][cur_j - 1] == ".":
            cur_j -= 1
    elif c == "R":
        if cur_j + 1 < w and grid[cur_i][cur_j + 1] == ".":
            cur_j += 1
    elif c == "U":
        if cur_i - 1 >= 0 and grid[cur_i - 1][cur_j] == ".":
            cur_i -= 1
    elif c == "D":
        if cur_i + 1 < h and grid[cur_i + 1][cur_j] == ".":
            cur_i += 1

print(cur_i + 1, cur_j + 1)