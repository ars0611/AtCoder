import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------
#入力
s = input()
t = input()

#DynamicProgramming
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]
for j in range(len(t)+1):
    dp[0][j] = j
for i in range(len(s)+1):
    dp[i][0] = i

#LevenshteinDistance(編集距離)
#sの1~i+1文字目の文字列からtのj+1文字目までの文字列を作る際の編集距離をdp[i][j]に格納
for i in range(1,len(s)+1):
    for j in range(len(t)+1):
        if i >= 1 and j >= 1 and s[i-1] == t[j-1]:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1])
        elif i >= 1 and j >= 1:
            dp[i][j] = min(dp[i-1][j] + 1, dp[i][j-1] + 1, dp[i-1][j-1] + 1)
        elif j >= 1:
            dp[i][j] = dp[i][j-1] + 1

#出力
print(dp[len(s)][len(t)])