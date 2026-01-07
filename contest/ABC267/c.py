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
preS = [0]
cnt = 0
for i in range(n):
    preS.append(preS[-1] + a[i])
    if i < m:
        cnt += (i + 1) * a[i]
ans = cnt
for i in range(n - m):
    cnt += a[i + m] * m - (preS[i + m] - preS[i])
    ans = max(ans, cnt)
print(ans)

