import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
cnt = 0
for i in range(N):
    A, B = map(int, input().split())
    if A < B:
        cnt += 1
print(cnt)