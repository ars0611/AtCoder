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
ans = 0
for i in range(N // 2 + N % 2):
    ans += A[2*i]
print(ans)