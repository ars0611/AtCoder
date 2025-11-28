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
mod = 998244353
n = int(input())
card = [list(map(int, input().split())) for _ in range(n)]
dp = [[0]*n for _ in range(2)]
dp[0][0] = 1
dp[1][0] = 1
for j in range(n - 1):
    for i in range(2):
        dp[i][j] %= mod
        for k in range(2):
            if card[j + 1][k] != card[j][i]:
                dp[k][j + 1] += dp[i][j]
print((dp[0][n - 1] + dp[1][n - 1]) % mod)
