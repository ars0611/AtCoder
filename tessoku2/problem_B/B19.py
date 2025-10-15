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
max_value = 10**2 * 10**3
max_weight = 10**9 + 1
for i in range(n):
    w_i, v_i = map(int ,input().split())
    weight.append(w_i)
    value.append(v_i)

dp = [[max_weight] * (max_value + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    for j in range(max_value + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j])
        if j + value[i - 1] <= max_value and dp[i - 1][j] != max_weight:
            dp[i][j + value[i - 1]] = min(dp[i][j + value[i - 1]], dp[i - 1][j] + weight[i - 1])


ans = 0
for j in range(max_value, - 1, -1):
    if dp[n][j] <= w:
        ans = j
        break
print(ans)