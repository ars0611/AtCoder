import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N,L,R = map(int, input().split())
W =[list(map(int, input().split())) for i in range(N)]
cnt = 0
for i in range(N):
    if W[i][0] <= L:
        if W[i][1] >= R:
            cnt += 1
print(cnt)