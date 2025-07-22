import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n, m = map(int, input().split())
ans = 0
for i in range(m+1):
    ans += n**i
if ans > 10**9:
    print("inf")
else:
    print(ans)