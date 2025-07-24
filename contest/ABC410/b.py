import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N, Q = map(int, input().split())
X = list(map(int, input().split()))
box = [0]*N
for i in X:
    if i >= 1:
        box[i-1] += 1
        print(i, end = " ")
    else:
        min = 0
        for j in range(N):
            if box[j] < box[min]:
                min = j
        box[min] += 1
        print(min+1, end= " ")