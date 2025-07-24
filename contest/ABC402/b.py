import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
Q = int(input())
w = deque()
for i in range(Q):
    q_i = list(map(int, input().split()))
    if q_i[0] == 1:
        w.append(q_i[1])
    else:
        print(w[0])
        w.popleft()