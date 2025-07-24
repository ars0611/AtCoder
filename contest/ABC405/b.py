import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N,M = map(int, input().split())
A = list(map(int, input().split()))



for i in range(N):
    for j in range(1,M+1):
        if not j in A:
            print(i)
            exit()
    A.pop()
print(N)