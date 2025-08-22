import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n = int(input())
s = list(input())
t = []
for s_i in s:
    if s_i == "R":
        t.append("P")
    elif s_i == "S":
        t.append("R")
    else:
        t.append("S")
# dp[0][i] := [出した手, i+1回目のじゃんけんであいこだったときの最大の勝利数
# dp[1][i] := [出した手, i+1回目のじゃんけんで勝ったときの最大の勝利数]
dp = [[[0,0]]*n for _ in range(2)]
dp[0][0] = [s[0], 0]
dp[1][0] = [t[0], 1]

for i in range(1,n):
    #i+1回目にあいこだったときの最大の勝利数
    if s[i] != dp[0][i-1][0] and s[i] != dp[1][i-1][0]:
        if dp[0][i-1][1] > dp[1][i-1][1]:
            dp[0][i] = [s[i], dp[0][i-1][1]]
        else:
            dp[0][i] = [s[i], dp[1][i-1][1]]
    elif s[i] == dp[0][i-1][0]:
        dp[0][i] = [s[i], dp[1][i-1][1]]
    else:
        dp[0][i] = [s[i], dp[0][i-1][1]]

    #i+1回目に勝ったときの最大の勝利数
    if t[i] != dp[0][i-1][0] and t[i] != dp[1][i-1][0]:
        if dp[0][i-1][1] > dp[1][i-1][1]:
            dp[1][i] = [t[i], dp[0][i-1][1] + 1]
        else:
            dp[1][i] = [t[i], dp[1][i-1][1] + 1]
    elif t[i] == dp[0][i-1][0]:
        dp[1][i] = [t[i], dp[1][i-1][1] + 1]
    else:
        dp[1][i] = [t[i], dp[0][i-1][1] + 1]

print(max(dp[0][n-1][1], dp[1][n-1][1]))

#これもっときれいに書けんのか？

#行を勝敗の状態でなく出した手で書けばうまかったらしい