import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n, m = map(int, input().split())
b = list(map(int, input().split()))
w = list(map(int, input().split()))

b.sort(reverse = True)
w.sort(reverse = True)
b_sum = [0]*(n+1)
w_sum = [0]*(m+1)
w_max = [0]*(m+1)
for i in range(1,n+1):
    b_sum[i] = b_sum[i-1] + b[i-1]
for i in range(1,m+1):
    w_sum[i] = w_sum[i-1] + w[i-1]
    w_max[i] = max(w_sum[i], w_max[i-1])

ans = 0
for i in range(n+1):
    ans = max(ans, b_sum[i] + w_max[min(i,m)])
print(ans)