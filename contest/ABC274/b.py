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
from functools import lru_cache
#----------------------------------------#
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
x = []
for j in range(w):
    cnt = 0
    for i in range(h):
        if grid[i][j] == "#":
            cnt += 1
    x.append(cnt)
print(*x)
