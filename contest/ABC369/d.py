import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
dp = [[0] * n for _ in range(2)]
dp[1][0] = a[0]
for i in range(1,n):
    dp[0][i] = max(dp[0][i-1], dp[1][i-1] + 2*a[i])
    dp[1][i] = max(dp[1][i-1], dp[0][i-1] + a[i])

print(max(dp[0][n-1], dp[1][n-1]))

#dp自力ACうれしい