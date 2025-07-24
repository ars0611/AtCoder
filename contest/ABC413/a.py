import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N,M = map(int, input().split())
A =list(map(int, input().split()))
sum = 0
for i in A:
  sum += i
if sum <= M:
  print("Yes")
else:
  print("No")