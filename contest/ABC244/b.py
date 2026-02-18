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
n = int(input())
t = input().strip()
x, y = 0, 0
d = 0
dx = [1, 0, -1, 0]
dy = [0, -1, 0, 1]
for ch in t:
    if ch == 'S':
        x += dx[d]
        y += dy[d]
    else:
        d += 1
        d %= 4
print(x, y)
