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
n, m = map(int, input().split())
rel = [0]*n
for _ in range(m):
    a, b = map(lambda x:int(x) - 1, input().split())
    rel[a] += 1
    rel[b] += 1
ans = []
for i in range(n):
    ans.append(math.comb(n - 1 - rel[i], 3))
print(*ans)
