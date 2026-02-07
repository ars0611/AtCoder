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
m = max(a)
d = [0] * (10 ** 6)
for i in range(n):
    d[-a[i]] += 1
for i in range(1, 10 ** 6):
    d[i] += d[i - 1]
for i in range(10 ** 6 - 1, -1, -1):
    if d[i] < 10: continue
    d[i - 1] += d[i] // 10
    d[i] %= 10
ans = [str(di) for di in d]
for i in range(10 ** 6):
    if ans[i] != '0':
        print(''.join(ans[i:]))
        break
