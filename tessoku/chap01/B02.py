import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#######################################回答########################################
a, b = map(int, input().split())
for i in range(a,b+1):
    if 100 % i == 0:
        print("Yes")
        exit()
print("No")