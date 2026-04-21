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
a = []
b = []
t = []
for _ in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    t.append(ai / bi)
l = 0
r = n - 1
cur = 0
while l != r:
    if t[l] <= t[r]:
        cur += b[l] * t[l]
        t[r] -= t[l]
        l += 1
    else:
        cur += b[l] * t[r]
        t[l] -= t[r]
        r -= 1
cur += b[l] * (t[l] / 2)
print(cur)
