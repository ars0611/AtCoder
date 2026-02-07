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
from functools import cmp_to_key
#----------------------------------------#
n, a, b = map(int, input().split())
grid = [['.'] * n * b for _ in range(n * a)]
for i in range(n):
    for j in range(n):
        for k in range(a):
            for l in range(b):
                if (i + j) % 2 == 1:
                    grid[i * a + k][j * b + l] = '#'
for i in range(n * a):
    print(''.join(grid[i]))
