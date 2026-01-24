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
n, k = map(int, input().split())
a = list(map(int, input().split()))
pos = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n):
    minD = 10 ** 11
    for ai in a:
        d = (pos[i][0] - pos[ai - 1][0]) ** 2 + (pos[i][1] - pos[ai - 1][1]) ** 2
        minD = min(minD, d)
    ans = max(ans, minD)
print(math.sqrt(ans))
