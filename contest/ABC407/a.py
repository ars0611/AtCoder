import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
A, B = map(int, input().split())
if A/B - A//B > 0.5:
    print(A//B+1)
else:
    print(A//B)