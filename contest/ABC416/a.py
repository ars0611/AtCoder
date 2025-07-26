import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n, l, r = map(int, input().split())
s = input()
for i in range(l-1,r):
    if s[i] == "x":
        print("No")
        exit()
print("Yes")