import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
Q = int(input())
A = deque()

for i in range(Q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c = query[1]
        x = query[2]
        A += [[c, x]]
    else:
        k = query[1]
        sum = 0
        while k != 0:
            c = A[0][0]
            x = A[0][1]    
            if c > k:
                sum += k * x
                A[0][0] -= k
                k = 0
            else:
                sum += c * x
                k -= c
                A.popleft()
        print(sum)