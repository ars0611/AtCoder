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
a = [list(map(int, input().split())) for _ in range(h)]
r = [0]*h
c = [0]*w
for i in range(h):
    for j in range(w):
        r[i] += a[i][j]
        c[j] += a[i][j]
b = [[0]*w for _ in range(h)]
for i in range(h):
    for j in range(w):
        b[i][j] += r[i] + c[j] - a[i][j]
for i in range(h):
    print(*b[i])
