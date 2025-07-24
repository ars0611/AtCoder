import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N, S = map(int, input().split())
T = list(map(int, input().split()))

if T[0] > S:
    print("No")
    exit()
for i in range(N-1):
    if T[i+1] - T[i] > S:
        print("No")
        exit()
print("Yes")