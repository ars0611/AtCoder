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
n, m = map(int, input().split())
a = []
for i in range(m):
    a_i = list(map(int, input().split()))
    a.append(a_i)

#bitdp
#dp[i][集合] := クーポンiまでをつかって無料である品の集合をつくるときの最小値。もちろん作れない場合もある。
#集合をjを二進変換したときの1であるビットで表す。
dp = [[10 ** 3]*(2**n) for _ in range(m+1)] #クーポン数mなのでmより十分大きい数で初期化
dp[0][0] = 0
for i in range(1,m+1):
    for j in range(2**n):
        
        #free[k] = True := 品物kはすでに無料である。
        free = [False]*n

        #jを二進変換した際に左からk+1番目のビットが立ってたらすでに無料
        for k in range(n):
            if (j // 2 ** k) % 2 == 1:
                free[k] = True

        #クーポンiを選んだ時のjを求める
        v = 0
        for k in range(n):
            if free[k] == True or a[i-1][k] == 1:
                v += 2 ** k

        #遷移
        dp[i][j] = min(dp[i][j], dp[i-1][j])
        dp[i][v] = min(dp[i][v], dp[i-1][j] + 1)

#出力
if dp[m][2**n -1] == 10**3:
    print(-1)
else:
    print(dp[m][2**n-1])