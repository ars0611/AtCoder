import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
S = list(input())
m = S.count("#")
for i in range(m // 2):
    cnt = 0
    for j in range(len(S)):
        if S[j] == "#" and cnt == 0:
            print(j+1, end=",")
            S[j] = "."
            cnt += 1
        elif S[j] == "#" and cnt == 1:
            print(j+1)
            S[j] ="."
            break