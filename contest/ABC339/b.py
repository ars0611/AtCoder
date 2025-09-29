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
grid = [["."]*w for _ in range(h)]
r = 0
curx = 0
cury = 0
for _ in range(n):
    if grid[cury][curx] == ".":
        grid[cury][curx] = "#"
        if r == 0:
            curx += 1
        elif r == 1:
            cury += 1
        elif r == 2:
            curx -= 1
        else:
            cury -= 1
        r += 1
    else:
        grid[cury][curx] = "."
        if r == 0:
            curx -= 1
        elif r == 1:
            cury -= 1
        elif r == 2:
            curx += 1
        else:
            cury += 1
        r -= 1
    r %= 4
    curx %= w
    cury %= h

for row in grid:
    print("".join(row))