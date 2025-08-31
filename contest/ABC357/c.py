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
grid = ["#"] # レベル0のgrid
for _ in range(n):
    newgrid = []
    white = "." * len(grid[0])
    for r in grid:
        newgrid.append(r * 3)
    for r in grid:
        newgrid.append(r + white + r)
    for r in grid:
        newgrid.append(r * 3)
    grid = newgrid

print("\n".join(grid))

# 下のレベルから順にレベルnまで作っていく。
# 3行に分けて追加していく感じ。