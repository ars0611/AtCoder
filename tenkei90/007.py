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
n = int(input())
a = sorted(list(map(int, input().split())))
q = int(input())
for _ in range(q):
    b = int(input())
    idx = bisect.bisect_left(a, b)
    l = b - a[idx - 1] if idx - 1 > -1 else 10 ** 9 + 1
    r = a[idx] - b if idx < n else 10 ** 9 + 1
    print(min(l, r))
