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
n, m = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))
b = [0] * (m + 1)
for i in range(m, -1, -1):
    w = c[n + i]
    for j in range(m - i):
        if n - (m - i) + j >= 0:
            w -= b[m - j] * a[n - (m - i) + j]
    b[i] = w // a[n]
print(*b)

# 多項式の割り算。次数が大きいほうから決めていくだけ。
