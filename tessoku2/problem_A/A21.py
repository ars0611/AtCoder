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
p = []
a = []
for _ in range(n):
    pi, ai = map(int, input().split())
    p.append(pi)
    a.append(ai)
dp = [[0]*(n + 2) for _ in range(n + 2)]
for i in range(1, n + 1):
    for j in range(n, i - 1, -1):
        score_l = 0
        score_r = 0
        if 2 <= i  and i - 1 <= p[i - 2] <= j:
            score_l = a[i - 2]
        if j <= n - 1 and i <= p[j] <= j + 1:
            score_r = a[j]
        dp[i][j] = max(dp[i - 1][j] + score_l, dp[i][j + 1] + score_r)
ans = 0
for i in range(1, n + 1):
    ans = max(ans, dp[i][i])
print(ans)