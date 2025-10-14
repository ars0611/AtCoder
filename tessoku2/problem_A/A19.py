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
n, w = map(int, input().split())
weight = []
value = []
for i in range(n):
    w_i, v_i = map(int, input().split())
    weight.append(w_i)
    value.append(v_i)
dp = [[-1] * (w + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(w + 1):
        if dp[i][j] == -1:
            dp[i][j] = dp[i - 1][j]
        if j + weight[i - 1] <= w and dp[i - 1][j] != -1:
            dp[i][j + weight[i - 1]] = max(dp[i - 1][j + weight[i - 1]], dp[i - 1][j] + value[i - 1])
print(max(dp[n]))