import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
S = input()
ans = []
for i in range(len(S)):
    if S[i].isupper():
        ans.append(S[i])
print("".join(ans))