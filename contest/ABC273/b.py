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
x, k = map(int, input().split())
for i in range(k):
    x //= 10 ** i
    if x % 10 > 4:
        x += (10 - x % 10)
    else:
        x -= x % 10
    x *= 10 ** i
print(x)
