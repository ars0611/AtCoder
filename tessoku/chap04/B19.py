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
n,w = map(int, input().split())
weight = [] #weight[i] := 品物i+1の重さ
value = [] #value[i] := 品物i+1の価値
for _ in range(n):
    w_i, v_i = map(int, input().split())
    weight.append(w_i)
    value.append(v_i)

#DynamicProgramming
#制約を利用してdpを初期化
dp = [[10 ** 9 + 1]*(1000 * 100 + 1) for _ in range(n+1)] 
dp[0][0] = 0
#dp[i][j] := 品物iまでを用いて,価値jを作る時の最小の重さを格納
#横軸：価値,縦軸：品物として,マスに重さを入れる表計算のイメージ
for i in range(1,n+1):
    for j in range(100 * 1000 + 1):
        
        if value[i-1] > j:
            dp[i][j] = dp[i-1][j]
        
        else:
            dp[i][j] = min(dp[i-1][j], dp[i-1][j - value[i-1]] + weight[i-1])


#価値が高いほうから見て重さが条件を満たしていたら、その価値を出力
for j in range(100 * 1000,-1,-1):
    if dp[n][j] <= w:
        print(j)
        exit()