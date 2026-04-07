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
n, m = map(int, input().split())
p = [tuple(map(lambda x: int(x) - 1, input().split())) for _ in range(m)]
graph = [[] for _ in range(n)]
for a, b in p:
    graph[a].append(b)
    graph[b].append(a)
