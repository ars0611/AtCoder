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
n = int(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]
m = 0
for xi, yi in pos:
    for xj, yj in pos:
        m = max(m, (xi - xj) ** 2 + (yi - yj) ** 2)
print(math.sqrt(m))
