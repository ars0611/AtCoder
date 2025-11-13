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
grid = list(input().strip() for _ in range(h))

for i in range(h):
    for j in range(w - 4):
        s = []
        t = []
        for k in range(5):
            s.append(grid[i][j + k])
            t.append(grid[i][j + 4 - k])
        if "".join(s) == "snuke":
            ans = [(i + 1, j + k + 1) for k in range(5)]
        if "".join(t) == "snuke":
            ans = [(i + 1, j + k + 1) for k in range(4, -1, -1)]

for j in range(w):
    for i in range(h - 4):
        s = []
        t = []
        for k in range(5):
            s.append(grid[i + k][j])
            t.append(grid[i + 4 - k][j])
        if "".join(s) == "snuke":
            ans = [(i + k + 1, j + 1) for k in range(5)]
        if "".join(t) == "snuke":
            ans = [(i + k + 1, j + 1) for k in range(4, -1, -1)]
                
for i in range(h - 4):
    for j in range(w - 4):
        s = []
        t = []
        for k in range(5):
            s.append(grid[i + k][j + k])
            t.append(grid[i + 4 - k][j + 4 - k])
        if "".join(s) == "snuke":
            ans = [(i + k + 1, j + k + 1) for k in range(5)]
        if "".join(t) == "snuke":
            ans = [(i + k + 1, j + k + 1) for k in range(4, -1, -1)]

for i in range(h - 4):
    for j in range(w - 1, 3, -1):
        s = []
        t = []
        for k in range(5):
            s.append(grid[i + k][j - k])
            t.append(grid[i + 4 - k][j - 4 + k])
        if "".join(s) == "snuke":
            ans = [(i + k + 1, j - k + 1) for k in range(5)]
        if "".join(t) == "snuke":
            ans = [(i + k + 1, j - k + 1) for k in range(4, -1, -1)]

for k in range(5):
    print(ans[k][0], ans[k][1])