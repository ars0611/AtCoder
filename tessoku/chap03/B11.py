import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
a.sort()
q = int(input())
for _ in range(q):
    x = int(input())
    idx = bisect.bisect_left(a,x)
    print(idx)