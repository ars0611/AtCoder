import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
ans = ["-"]*n
if n % 2 == 0:
    ans[n//2] = ans[n//2-1] = "="
else:
    ans[n//2] = "="
print("".join(ans))