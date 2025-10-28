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
cost = []
seat = []
for _ in range(n):
    x, y, z = map(int, input().split())
    cost.append(max(0, (y - x) // 2 + 1))
    seat.append(z)

dp = [[0] + [float("inf")] * (10**5) for _ in range(n + 1)]

for i in range(1,n + 1):
    for j in range(10 ** 5 + 1):
        dp[i][j] = min(dp[i - 1][j], dp[i][j])
        if j + seat[i - 1] <= 10 ** 5 and dp[i - 1][j] != float("inf"):
            dp[i][j + seat[i - 1]] = min(dp[i][j + seat[i - 1]], dp[i - 1][j] + cost[i - 1])

need = sum(seat) // 2 + 1
ans = float("inf")
for j in range(need, 10**5 + 1):
    ans = min(ans, dp[n][j])
print(ans)

# ナップサックDPできたのはいいけどなんか変じゃない？