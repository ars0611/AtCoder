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
n, s = map(int, input().split())
a = list(map(int, input().split()))

#dynamic programming
dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(1,n+1):
    for j in range(s+1):
        if j < a[i-1]:
            if dp[i-1][j] == True:
                dp[i][j] = True
        else:
            if dp[i-1][j] == True or dp[i-1][j-a[i-1]] == True:
                dp[i][j] = True

#合計をsにする組み合わせがない場合
if dp[n][s] == False:
    print(-1)
    exit()

#dp[n][s]から遡ってカードの選び方を得る
cur_i = n #現在地
cur_j = s #現在地
ans = []
for _ in range(n): #最大でもn枚のカードまでしか選べないため
    
    if cur_i == cur_j == 0: 
        break
    
    #カードcur_iを用いてない場合
    if dp[cur_i-1][cur_j] == True:
        cur_i -= 1
    
    #カードcur_iを用いている場合
    else:
        ans.append(str(cur_i))
        cur_j -= a[cur_i-1]
        cur_i -= 1

ans.reverse() #出力例が昇順なので一応
#出力
print(len(ans))
print(" ".join(ans))