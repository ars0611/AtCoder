import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, m = map(int, input().split())
coupon = []
for _ in range(m):
    a = list(map(int, input().split()))
    num = 0
    for i in range(n):
        if a[i] == 1:
            num += 2**i
    coupon.append(num)

dp = [[m + 1]*(1 << n) for _ in range(m + 1)]
dp[0][0] = 0
for i in range(1, m + 1):
    for j in range((1 << n)):
        dp[i][j] = min(dp[i][j], dp[i - 1][j])
        if dp[i - 1][(j ^ coupon[i - 1]) & j] != m + 1:
            dp[i][j] = min(dp[i][j], dp[i - 1][(j ^ coupon[i - 1]) & j] + 1)

print(dp[m][(1 << n) - 1] if dp[m][(1 << n) - 1] != m + 1 else - 1)