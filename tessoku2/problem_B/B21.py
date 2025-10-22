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
s = input().strip()

# 初期化
dp = [[0]*n for _ in range(n)]
for i in range(n): 
    dp[i][i] = 1
for i in range(n - 1): 
    if s[i] == s[i + 1]:
        dp[i][i + 1] = 2
    else:
        dp[i][i + 1] = 1

# 短い方から作ってく
for length in range(2, n):
    for l in range(n - length):
        r = l + length
        if s[l] == s[r]:
            dp[l][r] = max(dp[l][r - 1], dp[l + 1][r], dp[l + 1][r - 1] + 2)
        else:
            dp[l][r] = max(dp[l][r - 1], dp[l + 1][r])
print(dp[0][n - 1])

# これやってることはわかるけど自分で考察からやるの無理だな