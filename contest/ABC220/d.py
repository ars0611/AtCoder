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
a = list(map(int, input().split()))
dp = [[0]*(10) for _ in range(n - 1)]
dp[0][(a[0] + a[1]) % 10] += 1
dp[0][(a[0] * a[1]) % 10] += 1
for i in range(0, n - 2):
    for j in range(10):
        dp[i + 1][(j + a[i + 2]) % 10] += dp[i][j]
        dp[i + 1][(j * a[i + 2]) % 10] += dp[i][j]
        dp[i + 1][(j + a[i + 2]) % 10] %= mod
        dp[i + 1][(j * a[i + 2]) % 10] %= mod
for k in range(10):
    print(dp[-1][k] % mod)
