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
mod = 998244353
n = int(input())
d = len(str(n))
ans = 0
for p in range(d - 1):
    ans += 9 * 10 ** p * (1 + 9 * 10 ** p) // 2
    ans %= mod
ans += (n - 10 ** (d - 1) + 1) * (1 + n - 10 ** (d - 1) + 1) // 2
ans %= mod
print(ans)
