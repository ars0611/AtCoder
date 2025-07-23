import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())
s = input()
t = input()
cnt = 0
for i in range(n):
    if s[i] != t[i]:
        cnt += 1
print(cnt)