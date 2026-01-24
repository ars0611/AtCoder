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
a = sorted(list(map(int, input().split())))
preSum = [0]
for i in range(n):
    preSum.append(preSum[-1] + a[i])
sumA = sum(a)
for _ in range(q):
    x = int(input())
    idx = bisect.bisect_left(a, x)
    ans = x * n - preSum[n] if idx == n else x * idx - preSum[idx] + preSum[n] - preSum[idx] - x * (n - idx)
    print(ans)
