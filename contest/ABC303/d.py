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
x, y, z = map(int, input().split())
s = input().strip()
n = len(s)

dp = [[0]*(n + 1) for _ in range(2)] # i == 0 : Off, i == 1 : on
dp[1][0] = z
for i in range(n):
    if s[i].isupper():
        dp[0][i + 1] = min(dp[0][i] + y, dp[1][i] + z + min(x, y))
        dp[1][i + 1] = min(dp[0][i] + z + min(x, y), dp[1][i] + x)
    else:
        dp[0][i + 1] = min(dp[0][i] + x, dp[1][i] + z + min(x, y))
        dp[1][i + 1] = min(dp[0][i] + z + min(x, y), dp[1][i] + y)

print(min(dp[0][n], dp[1][n]))