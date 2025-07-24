import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N, K = map(int, input().split())
A = list(map(int, input().split()))
ans = 1
for i in A:
    ans *= i
    if ans >= 10**K:
        ans = 1
print(ans)