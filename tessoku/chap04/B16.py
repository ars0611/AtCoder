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
h = list(map(int, input().split()))

dp = [0]*n
dp[1] = abs(h[1]-h[0])
for i in range(2,n):
    dp[i] = min(dp[i-2] + abs(h[i] - h[i-2]), dp[i-1] + abs(h[i] - h[i-1]))
print(dp[n-1])