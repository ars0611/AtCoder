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
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0]*n
for i in range(1,n):
    if i == 1:
        dp[i] = a[0]
    else:
        dp[i] = min(a[i-1] + dp[i-1], b[i-2] + dp[i-2])
print(dp[n-1])