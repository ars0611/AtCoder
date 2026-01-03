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

rootN = math.isqrt(n)
sq = []
for i in range(1, rootN + 1):
    sq.append(i ** 2)

ans = set()
ng = set()
for i in range(len(sq) - 1):
    for j in range(i + 1, len(sq)):
        k = sq[i] + sq[j]
        if k > n or k in ng: continue
        if k in ans:
            ans.discard(k)
            ng.add(k)
        else:
            ans.add(k)

ans = sorted(list(ans))
print(len(ans))
print(*ans)
