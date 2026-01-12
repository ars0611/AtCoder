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
mod = 998244353
n = int(input())
a = list(map(int, input().split()))
ans = 0
for i in range(1, n + 1):
    dp = [[[0]*(n + 1) for _ in range(n + 1)] for __ in range(n + 1)]
    dp[0][0][0] = 1
    for j in range(n):
        for k in range(n):
            for l in range(n):
                if i != k:
                    dp[j + 1][k + 1][(l + a[j]) % i] += dp[j][k][l]
                dp[j + 1][k][l] += dp[j][k][l]
    ans += dp[n][i][0]
print(ans % mod)

# mod i固定でjまでk個使って作った和mod iの個数
# すなわち使う個数固定か
