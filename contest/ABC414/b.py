import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
W = [list(input().split()) for i in range(N)]
S = []
sum = 0
for i in range(N):
    W[i][1] = int(W[i][1])
    sum += W[i][1]

if sum <= 100:
    for i in range(N):
        S += W[i][0] * W[i][1]
    print ("".join(S))
else:
    print("Too Long")