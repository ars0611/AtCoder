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
n, k = map(int, input().split())
a = list(map(int, input().split()))

#累積和をとる
sum= [0]*(n+1)
for i in range(n):
    sum[i+1] = sum[i] + a[i]

#しゃくとり法
r = [0]*n
for i in range(n):
    if i == 0:
        r[i] = 0
    else:
        r[i] = r[i-1]
    while r[i] < n and sum[r[i] + 1] - sum[i] <= k:
        r[i] += 1

ans = 0
for i in range(n):
    ans += r[i]-i
print(ans)