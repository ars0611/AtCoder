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
n, x, y = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (10 * n * 2 + 1) for _ in range(n + 1)]
dp[0][10 * n] = True
dp[1][10 * n + a[0]] = True
for i in range(n - 1):
    for j in range(10 * n * 2 + 1):
        if not dp[i][j]: continue
        dp[i + 2][j + a[i + 1]] = True
        dp[i + 2][j - a[i + 1]] = True
if n % 2 == 0:
    print("Yes" if dp[n][10 * n + y] and dp[n - 1][10 * n + x] else "No")
else:
    print("Yes" if dp[n][10 * n + x] and dp[n - 1][10 * n + y] else "No")
