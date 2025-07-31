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
p = [None]*n
a = [None]*n
for i in range(n):
    p[i],a[i] = map(int,input().split())
    
#DynamicProgramming
dp = [[None]*(n+1) for _ in range(n+1)]
dp[1][n] = 0
#dp[l][r] := ブロックがlからrまでのこってる時の最大の得点
#lからrまでの長さをlenとする
for len in range(n-2, -1, -1):
    for l in range(1, n-len+1):
        r = l + len

        #l-1番目のブロックを取り除いた時の得点
        score_l = 0
        if l >= 2 and l <= p[l-2] and p[l-2] <= r:
            score_l = a[l-2]
        
        #r+1番目のブロックを取り除いた時の得点
        score_r = 0
        if r <= n-1 and l <= p[r] and p[r] <= r:
            score_r = a[r]

        #dp[l][r]を求める
        if l == 1:
            dp[l][r] = dp[l][r+1] + score_r
        elif r == n:
            dp[l][r] = dp[l-1][r] + score_l
        else:
            dp[l][r] = max(dp[l-1][r] + score_l, dp[l][r+1] + score_r)

#出力
ans = 0
for i in range(1,n+1):
    ans = max(ans, dp[i][i])
print(ans)