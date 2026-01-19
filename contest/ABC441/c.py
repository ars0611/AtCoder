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
n, k, x = map(int, input().split())
a = sorted(list(map(int, input().split())))
s = [0]
for i in range(n):
    s.append(s[-1] + a[i])
if s[k] < x:
    print(-1)
else:
    ans = -1
    for m in range(n - k + 1, n + 1):
        alc = s[k] - s[n - m]
        if alc >= x:
            ans = m
            break
    print(ans)
