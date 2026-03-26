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
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = [[0]*h for _ in range(w)]
for i in range(w):
    for j in range(h):
        b[i][j] = a[j][i]
for i in range(w):
    print(*b[i])
