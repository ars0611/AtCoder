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
s = input()
t = input()

#DynamicProgramming
#dp[i][j] := sのi文字目までとtのj文字目までで作れるLCS（最長共通部分列）
dp = [[0]*(len(t)+1) for _ in range(len(s)+1)]

for i in range(1,len(s)+1):
    for j in range(len(t)+1):
        if i >= 1 and j >= 1 and s[i-1] == t[j-1]:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1], dp[i-1][j-1] + 1)
        elif i >= 1 and j >= 1:
            dp[i][j] = max(dp[i-1][j], dp[i][j-1])
        elif i >= 1:
            dp[i][j] = dp[i-1][j]

print(dp[len(s)][len(t)])