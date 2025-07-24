import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
x = float(input())

if x >= 38:
    print(1)
elif x >= 37.5:
    print(2)
else:
    print(3)