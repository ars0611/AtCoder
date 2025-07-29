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

#dp
dp = [[False]*(s+1) for _ in range(n+1)]
dp[0][0] = True
for i in range(1,n+1):
    for j in range(s+1):
        if j >= a[i-1]:
            if(dp[i-1][j] == True or dp[i-1][j-a[i-1]] == True):
                dp[i][j] = True
        else: 
            if dp[i-1][j] == True:
                dp[i][j] = True

#出力
if dp[n][s] == True:
    print("Yes")
else:
    print("No")