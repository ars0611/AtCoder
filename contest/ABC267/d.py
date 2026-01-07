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
inf = -2 * 10 ** 5 * 2000
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[inf] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m):
        if dp[i][j] == inf: continue
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (j + 1) * a[i])
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
print(dp[n][m])
for i in range(n + 1):
    print(*dp[i])

# 惜しい気がする
