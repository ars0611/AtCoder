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
mod = 998244353
n = int(input())
dp = [[0]*n for _ in range(9)]
for i in range(9):
    dp[i][0] = 1
for j in range(1, n):
    for i in range(9):
        if i == 0:
            dp[i][j] = dp[i][j - 1] + dp[i + 1][j - 1]
        elif i == 8:
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1]
        else:
            dp[i][j] = dp[i - 1][j - 1] + dp[i][j - 1] + dp[i + 1][j - 1]
        dp[i][j] %= mod
ans = 0
for i in range(9):
    ans += dp[i][n - 1]
    ans %= mod
print(ans)
