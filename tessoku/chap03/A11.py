import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n, x = map(int, input().split())
a = list(map(int, input().split()))

idx = bisect.bisect_right(a,x)
print(idx)