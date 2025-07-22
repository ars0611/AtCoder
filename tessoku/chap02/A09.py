import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
h,w,n = map(int, input().split())
s = [[0]*(w+1) for _ in range(h+1)]
#差分の累積和を取るとうまくいきそう
for _ in range(n):
