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
a = list(map(int, input().split()))
b = list(map(int, input().split()))

#DynamicProgramming
dp = [0]*n
for i in range(1,n-1):
    dp[a[i-1]-1] = max(dp[a[i-1]-1], dp[i] + 100)
    dp[b[i-1]-1] = max(dp[b[i-1]-1], dp[i] + 150)

#出力
print(dp[n-1])