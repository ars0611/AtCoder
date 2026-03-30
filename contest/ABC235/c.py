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
n, q = map(int, input().split())
a = list(map(int, input().split()))
query = [tuple(map(int, input().split())) for _ in range(q)]
d = defaultdict(list)
for i in range(n):
    d[a[i]].append(i + 1)
for x, k in query:
    print(d[x][k - 1] if k <= len(d[x]) else -1)
