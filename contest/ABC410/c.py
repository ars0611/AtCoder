import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N,Q = map(int, input().split())
A = [i for i in range(1,N+1)]
m = 0
for i in range(Q):
    query = list(map(int,input().split()))
    if query[0] == 1:
        A[query[1] -1 -m] = query[2]
    elif query[0] == 2:
        print(A[query[1] -1 -m])
    else:
        m -= query[1]
        m %= N