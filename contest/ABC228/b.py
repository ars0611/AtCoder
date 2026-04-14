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
n, x = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))
cur = x - 1
flgs = [False]*n
flgs[cur] = True
while not flgs[a[cur]]:
    cur = a[cur]
    flgs[cur] = True
print(flgs.count(True))
