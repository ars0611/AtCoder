import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
Distance = [0]
D = list(map(int, input().split()))
for i in range(N-1):
    Distance.append(Distance[i] + D[i])

    
for i in range(1,N-1):
    D[i] = D[i-1] + D[i]
    
for i in range(N-1):
    for j in range(i+1,N):
        if j == N-1:
            print(Distance[j] - Distance[i], sep="\n")
        else:
            print(Distance[j] - Distance[i], end=" ")