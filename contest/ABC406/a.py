import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
A, B, C, D = map(int, input().split())
if A > C:
    print("Yes")
elif A == C and B > D: 
    print("Yes")
else:
    print("No")