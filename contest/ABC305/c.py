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

ci = list()
cj = list()
for i in range(h):
    for j in range(w):
        if grid[i][j] == "#":
            ci.append(i)
            cj.append(j)

a = min(ci)
b = max(ci)
c = min(cj)
d = max(cj)
for i in range(h):
    for j in range(w):
        if grid[i][j] == "." and a <= i <= b and c <= j <= d:
            print(i + 1, j + 1)
            exit()