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
#----------------------------------------#
grid = [input().strip() for _ in range(9)]
poal = set()
for i in range(9):
    for j in range(9):
        if grid[i][j] == ".": continue
        poal.add((i, j))
ans = set()
for r, c in poal:
    for i in range(-9, 10, 1):
        for j in range(-9, 10, 1):
            if i == j == 0: continue
            pp = (r + i, c + j)
            ppp = (r + j, c - i)
            pppp = (pp[0] + j, pp[1] - i)
            if pp in poal and ppp in poal and pppp in poal:
                s = tuple(sorted([(r, c), pp, ppp, pppp]))
                ans.add(s)
print(len(ans))
