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
h, w = map(int, input().split())
grid = [list(input().strip()) for _ in range(h)]

for i in range(h):
    for j in range(w - 1):
        if grid[i][j] != "T": continue
        if grid[i][j] == grid[i][j + 1]:
            grid[i][j] = "P"
            grid[i][j + 1] = "C"

for i in range(h):
    print("".join(grid[i]))