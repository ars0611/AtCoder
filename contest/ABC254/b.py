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
a = [[0]*(i + 1) for i in range(n)]
a[0][0] = 1
for i in range(1, n):
    for j in range(i + 1):
        a[i][j] = 1 if j == 0 or j == i else a[i - 1][j - 1] + a[i - 1][j]
for i in range(n):
    print(*a[i])
