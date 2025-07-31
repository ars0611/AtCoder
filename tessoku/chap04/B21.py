import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
#入力
n = int(input())
s = input()

#DyanmicProgrammnig
dp = [[None]*n for _ in range(n)]

#l文字目からr文字目で作れる最長の回文で区間DP
#初期化
for i in range(n):
    dp[i][i] = 1
for i in range(n-1):
    if s[i] == s[i+1]:
        dp[i][i+1] = 2
    else:
        dp[i][i+1] = 1

#狭い区間から広げていく
for len in range(2,n):
    for l in range(n-len):
        r = l + len
        if s[l] == s[r]:
            dp[l][r] = max(dp[l][r-1], dp[l+1][r], dp[l+1][r-1] + 2)
        else:
            dp[l][r] = max(dp[l][r-1], dp[l+1][r])

#出力
print(dp[0][n-1])