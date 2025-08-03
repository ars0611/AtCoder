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
k = int(input())
s = input()
t = input()

#文字数の差がkを超えるとき、編集距離は必ずkを超える
if abs(len(s) - len(t)) > k:
    print("No")
    exit()

#dynamicprogramming
#編集距離がkを超える範囲は計算する必要がないことからその範囲だけをdpする
dp = [[10**9]*(2*k+1) for _ in range(len(s)+1)]

#編集距離
for i in range(len(s)+1):
    for d in range(2*k+1):
        
        #tのidx
        j = i + d - k
        if 0 <= j <= len(t):    
            
            #初期化    
            if i == 0 and  j == 0:
                dp[i][d] = 0
            elif i == 0:    
                dp[i][d] = j
            elif j == 0:
                dp[i][d] = i

            #次に追加する文字が同じ文字かどうかで場合分け
            elif s[i-1] == t[j-1]:
                
                #dの値によって前の計算のどこを使うかが変わるので場合分け
                if d == 0:
                    dp[i][d] = min(dp[i-1][d], dp[i-1][d+1] + 1)
                elif d == 2*k:
                    dp[i][d] = min(dp[i-1][d], dp[i][d-1] + 1)
                else:
                    dp[i][d] = min(dp[i-1][d], dp[i-1][d+1] + 1, dp[i][d-1] + 1)
                
            else:
                if d == 0:
                    dp[i][d] = min(dp[i-1][d] + 1, dp[i-1][d+1] + 1)
                elif d == 2*k:
                    dp[i][d] = min(dp[i-1][d] + 1, dp[i][d-1] + 1)
                else:
                    dp[i][d] = min(dp[i-1][d] + 1, dp[i-1][d+1] + 1, dp[i][d-1] + 1)

#出力
if dp[len(s)][len(t)-len(s)+k] <= k:
    print("Yes")
else:
    print("No")
