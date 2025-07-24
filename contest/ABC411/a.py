import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
P = input()
L = int(input())
if len(P) >= L:
    print("Yes")
else:
    print("No")