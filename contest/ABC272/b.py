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
n, m = map(int, input().split())
flg = [[False]*(n) for _ in range(n)]
for _ in range(m):
    k, *x = list(map(int, input().split()))
    for i in range(k):
        for j in range(k):
            flg[x[i] - 1][x[j] - 1] = True
print("Yes" if all(flg[i][j] for i in range(n) for j in range(n)) else "No")
