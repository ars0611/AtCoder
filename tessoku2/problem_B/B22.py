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
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [float("inf")]*n
dp[0] = 0
for i in range(n - 1):
    if dp[i] == float("inf"): continue
    dp[i + 1] = min(dp[i + 1], dp[i] + a[i])
    if i < n - 2:
        dp[i + 2] = min(dp[i + 2], dp[i] + b[i])
print(dp[n - 1])