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
grid = [list(map(int, input().split())) for _ in range(9)]

cmp = True
for i in range(9):
    if len(set(grid[i])) != 9:
        cmp = False
        break

for j in range(9):
    l = set()
    for i in range(9):
        l.add(grid[i][j])
    if len(l) != 9:
        cmp = False
        break

group = [set() for _ in range(9)]
for i in range(9):
    for j in range(9):
        group[i // 3 * 3 + j // 3].add(grid[i][j])
for i in range(9):
    if len(group[i]) != 9:
        cmp = False
        break
print("Yes" if cmp else "No")