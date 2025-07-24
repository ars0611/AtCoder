import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
R,X = map(int, input().split())
if X == 1 and 1600 <= R <= 2999:
    print("Yes")
elif X == 2 and 1200 <= R <= 2399:
    print("Yes")
else:
    print("No")