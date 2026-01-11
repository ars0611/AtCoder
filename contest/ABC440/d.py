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
n, q = map(int, input().split())
a = sorted([0] + list(map(int, input().split())))
d = []
d = [a[i + 1] - a[i] - 1 for i in range(n)]
s = [0]
for i in range(n):
    s.append(s[-1] + d[i])
for _ in range(q):
    x, y = map(int, input().split())
    idx = bisect.bisect_left(a, x)
    if idx == n + 1:
        print(x + y - 1)
        continue
    if y <= a[idx] - x:
        print(x + y - 1)
        continue
    y -= a[idx] - x
    iidx = bisect.bisect_left(s, s[idx] + y)
    if iidx == n + 1:
        print(a[n] + (y - (s[n] - s[idx])))
    else:
        print(a[iidx - 1] + s[idx] + y - s[iidx - 1])
