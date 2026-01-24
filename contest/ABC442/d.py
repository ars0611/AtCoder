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
n, q = map(int, input().split())
a = list(map(int, input().split()))
preSum = [0]
for ai in a:
    preSum.append(preSum[-1] + ai)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        ax = preSum[x + 1] - preSum[x]
        preSum[x] = preSum[x - 1] + ax
    else:
        print(preSum[query[2]] - preSum[query[1] - 1])
