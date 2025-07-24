import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
S = input()
cnt = 0
for i in range(1,len(S)+1):
    if i == 1:
        cnt += int(S[-i])
    else:
        cnt += (int(S[-i]) - int(S[-i+1])) % 10
cnt += len(S)
print(cnt)