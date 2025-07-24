import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
A = list(map(int, input().split()))
ans = 0
for i in range(101):
    cnt = 0
    for j in A:
        if j >= i:
            cnt += 1
    if cnt >= i and ans <= i:
        ans = i
print(ans)