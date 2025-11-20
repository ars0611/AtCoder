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
a = [list(map(int, input().split())) for _ in range(h)]

grid = [["."]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        if a[i][j] == 0: continue
        grid[i][j] = chr(a[i][j] - 1 + ord("A"))

for row in grid:
    print("".join(row))
