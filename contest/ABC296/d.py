import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**9)
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
n, m = map(int, input().split())
if n ** 2 < m:
    print(-1)
else:
    inf = n ** 2 + 1
    ans = inf
    max_a = math.isqrt(m) + 1
    for a in range(1, max_a + 1):
        b = (m - 1) // a + 1
        if b <= n:
            ans = min(ans, a * b)
    print(ans)