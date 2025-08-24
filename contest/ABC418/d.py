import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
t = input()

# 0の個数が偶数個のとき、美しい文字列なのでそれを数えたい
# dp[0][i] := 1,2,...i+1文字目からi+1文字目まで取り出したときに、0の個数が偶数個の文字列の数
# dp[1][i] := 1,2,...i+1文字目からi+1文字目まで取り出したときに、0の個数が奇数個の文字列の数
dp = [[0]*n for _ in range(2)]
if t[0] == "0":
    dp[1][0] = 1
else:
    dp[0][0] = 1

for i in range(1, n):
    if t[i] == "0":
        dp[0][i] = dp[1][i-1]
        dp[1][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = dp[0][i-1] + 1
        dp[1][i] = dp[1][i-1]

print(sum(dp[0]))

#1の個数と文字列の和の偶奇に着目しても美しい美しくないが言えたけど、実装が重たくなって詰んでた