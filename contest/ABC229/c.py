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
n, w = map(int, input().split())
cheese = list(tuple(map(int, input().split())) for _ in range(n))
cheese.sort(reverse=True)
cur = 0
ans = 0
for ai, bi in cheese:
    if cur > w: break
    ans += ai * min(bi, w - cur)
    cur += min(bi, w - cur)
print(ans)
