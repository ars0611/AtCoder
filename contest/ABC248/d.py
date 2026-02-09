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
a = list(map(int, input().split()))
pos = defaultdict(list)
for i in range(n):
    pos[a[i]].append(i + 1)
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
for l, r, x in query:
    print(bisect.bisect_right(pos[x], r) - bisect.bisect_left(pos[x], l))
