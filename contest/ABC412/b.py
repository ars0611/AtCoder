import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
S = input()
T = input()
for i in range(1,len(S)):
    if S[i].isupper() and not S[i-1] in T:
        print("No")
        exit()
print("Yes")