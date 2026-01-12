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
x = list(map(int, input().split()))
bonus = defaultdict(int)
for _ in range(m):
    c, y = map(int, input().split())
    bonus[c] = y
dp = [[-1]*(n + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    for j in range(n):
        if dp[i][j] == -1: continue
        dp[i + 1][j + 1] = max(dp[i + 1][j + 1], dp[i][j] + x[i] + bonus[j + 1])
        dp[i + 1][0] = max(dp[i + 1][0], dp[i][j])
print(max(dp[n]))
