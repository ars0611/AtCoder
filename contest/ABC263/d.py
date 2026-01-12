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
n, l, r = map(int, input().split())
a = list(map(int, input().split()))

dpl = [0]*(n + 1)
dpr = [0]*(n + 1)
for i in range(n):
    dpl[i + 1] = min(dpl[i] + a[i], l * (i + 1))
    dpr[i + 1] = min(dpr[i] + a[n - i - 1], r * (i + 1))
ans = sum(a)
for i in range(n + 1):
    ans = min(ans, dpl[i] + dpr[n - i])
print(ans)
