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
#----------------------------------------#
n = int(input())

dp = [[0]*(n + 1) for _ in range(2)] # i = 0 => 健康、#i = 1 => 毒盛られ
for i in range(n):
    x, y = map(int, input().split())
    if x == 1:
        dp[0][i + 1] = dp[0][i]
        dp[1][i + 1] = max(dp[0][i] + y, dp[1][i])
    else:
        dp[0][i + 1] = max(dp[1][i] + y, dp[0][i])
        dp[1][i + 1] = max(dp[1][i] + y, dp[1][i])

print(max(dp[0][n], dp[1][n]))