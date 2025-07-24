import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N, M = map(int,input().split())
W = [0]*(N+1) 
C = [list(map(int, input().split())) for _ in range(M)]
#城壁i+1を守る砲台数がiよりいくつ多いかをW[i+1]に格納する
for i in range(M):
    L = C[i][0]
    R = C[i][1]
    W[L] += 1
    if R != N:
        W[R+1] -= 1

#城壁iを守る砲台数をW[i]に格納する
for i in range(1,N+1):
    W[i] += W[i-1]

print(min(W[1:N+1]))