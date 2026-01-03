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
s = [input().strip() for _ in range(10)]
a = 11
b = -1
c = 11
d = -1
for i in range(10):
    for j in range(10):
        if s[i][j] == "#":
            a = min(a, i + 1)
            b = max(b, i + 1)
            c = min(c, j + 1)
            d = max(d, j + 1)
print(a, b)
print(c, d)
