import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
s = input()
cnt = 0

next ="i"
for i in s:
    if i == next:
        if next == "i":
            next = "o"
        else:
            next = "i"
    else:
        cnt += 1
if next == "o":
    cnt += 1
print(cnt)