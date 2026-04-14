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
n, k = map(int, input().split())
p = [list(map(int, input().split())) for _ in range(n)]
s = [sum(p[i]) for i in range(n)]
r = sorted(s)
for i in range(n):
    idx = bisect.bisect_right(r, s[i] + 300)
    rank = n - idx
    print("Yes" if rank + 1 <= k else "No")
