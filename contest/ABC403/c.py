import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N, M, Q = map(int, input().split())
auth = [set() for _ in range(N)]
all = ["f" for _ in range(N)]
for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]-1
        y = query[2]-1
        auth[x].add(y)
    elif query[0] == 2:
        x= query[1]-1
        all[x] = "t"
    else:
        x = query[1]-1
        y = query[2]-1
        if all[x] == "t" or y in auth[x]:
            print("Yes")
        else:
            print("No")