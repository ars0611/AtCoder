import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
X,Y = map(int, input().split())
cnt = 0
for i in range(1,7):
    for j in range(1,7):
        if i + j < X and abs(i-j) < Y:
            cnt += 1

print(1 - cnt/36)