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
n, m, k = map(int, input().split())
dp = [[0]*(k + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(k):
        for l in range(1, m + 1):
            if j + l <= k:
                dp[i + 1][j + l] += dp[i][j]
ans = sum(dp[n])
print(ans % mod)

# 配るDP
# 第i項までの和であとの項の数が決まるため、DPで解けるってわけ
# 第i項まで使って和がjになるパターン数を、次の項の値を決めて配っていく

