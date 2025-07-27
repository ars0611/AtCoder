import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#######################################回答########################################
t = int(input())
n = int(input())
sum = [0 for _ in range(t+1)]
e = [0 for _ in range(t+1)]
for i in range(n):
    l, r = map(int, input().split())
    e[l] += 1
    e[r] -= 1

for i in range(t+1):
    if i == 0:
        sum[i] = e[i]
    else:
        sum[i] = sum[i-1] + e[i]

for i in range(t):
    print(sum[i])