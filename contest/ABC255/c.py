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
x, a, d, n = map(int, input().split())
left = a if d > 0 else a + d * (n - 1)
right = a + d * (n - 1) if d > 0 else a
if x <= left:
    ans = left - x
elif left < x < right:
    ans = min((x - a) % abs(d), abs(d) - (x - a) % abs(d))
else:
    ans = x - right
print(ans)
