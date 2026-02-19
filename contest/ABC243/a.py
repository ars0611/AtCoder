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
v, a, b, c = map(int, input().split())
while True:
    if v < a:
        ans = 'F'
        break
    else:
        v -= a
    if v < b:
        ans = 'M'
        break
    else:
        v -= b
    if v < c:
        ans = 'T'
        break
    else:
        v -= c
print(ans)
