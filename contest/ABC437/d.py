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
#----------------------------------------#
mod = 998244353
n, m = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))
preSumB = [0]
for i in range(m):
    preSumB.append(preSumB[-1] + b[i])
    preSumB[i + 1] %= mod

ans = 0
for i in range(n):
    idx = bisect.bisect_left(b, a[i])
    ans += a[i] * (idx) - preSumB[idx] + preSumB[-1] - preSumB[idx] - a[i] * (m - idx)
    ans %= mod
print(ans % mod)
