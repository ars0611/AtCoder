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
n, t = map(int, input().split())
a = [0] + list(map(int, input().split())) + [t]
ans = 0
i = 1
cur = 0
while i - 1 <= n:
    ans += a[i] - cur
    cur = a[i] + 100
    i = bisect.bisect_left(a, cur)
print(ans)
