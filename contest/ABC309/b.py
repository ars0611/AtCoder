import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
n = int(input())
grid = [list(input().strip()) for _ in range(n)]

for i in range(n):
    if i == 0:
        print("".join(grid[i + 1][0:1] + grid[i][0:n - 1]))
    elif i < n - 1:
        print("".join(grid[i + 1][0:1] + grid[i][1:n - 1] + grid[i - 1][n - 1:n]))
    else:
        print("".join(grid[i][1:] + grid[i - 1][n - 1:n]))