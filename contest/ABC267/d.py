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
inf = -2 * 10 ** 5 * 2000 * 2000 - 1
n, m = map(int, input().split())
a = list(map(int, input().split()))
dp = [[inf] * (m + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(m + 1):
        if dp[i][j] == inf: continue
        dp[i + 1][j] = max(dp[i + 1][j], dp[i][j])
        if j < m:
            dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + (j + 1) * a[i])
print(dp[n][m])

# infの取り方適当でペナるのはもったいないので上限・下限の見積もりは正しくやろう
