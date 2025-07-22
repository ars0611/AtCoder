import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
a = int(input())
if 400 % a != 0:
    print(-1)
    exit()
print(400 // a)