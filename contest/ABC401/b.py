import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#--------------------��--------------------#
n = int(input())
cnt = 0
comp = False
for _ in range(n):
    s = input()
    if s == "login":
        comp = True
    elif s == "logout":
        comp = False
    elif s == "private":
        if not comp:
            cnt += 1
print(cnt)