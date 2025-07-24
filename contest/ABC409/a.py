import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
T = input()
A = input()

for i in range(N):
    if T[i] == A[i] == "o":
        print("Yes")
        exit()
print("No")