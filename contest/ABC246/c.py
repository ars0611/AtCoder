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
n, k, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
discounted = a[:]
i = n - 1
while k != 0 and i > -1:
    if a[i] <= k * x:
        discounted[i] = a[i] - x * (a[i] // x)
        k -= a[i] // x
    else:
        discounted[i] = a[i] - k * x
        k = 0
    i -= 1
discounted.sort()
while k != 0 and discounted:
    discounted.pop()
    k -= 1
print(sum(discounted))
