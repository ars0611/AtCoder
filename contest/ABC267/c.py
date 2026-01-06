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
a = list(map(int, input().split()))
preSi = [0]
preSm = [0]
for i in range(n):
    preSi.append(preSi[-1] + (i + 1) * a[i])
    preSm.append(preSm[-1] + m * a[i])
ans = -1
for i in range(n - m + 1):
    ans = max(ans, preSi[m + i] - preSi[i] - (preSm[m + i] - preSm[i]))
print(ans)

# なんだこれわかんね寝るわ
