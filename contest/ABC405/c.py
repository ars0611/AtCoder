import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
A = list(map(int, input().split()))

B = []
#BにA[0:i]までの和を格納
for i in range(N):
    if i == 0:
        B.append(A[0])
    else:
        B.append(B[i-1] + A[i])
ans = 0
for i in range(N-1):
    ans += A[i]*(B[-1] - B[i])
print(ans)