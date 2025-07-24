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
A.sort()
ans = set(A)
print(len(ans))
for i in ans:
    print(i, end=" ")