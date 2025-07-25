import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
q = int(input())
stack = [0]*100
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        stack.append(query[1])
    else:
        ans = stack.pop(-1)
        print(ans)