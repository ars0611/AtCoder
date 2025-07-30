import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
n, m = map(int, input().split())
s = [list(input()) for _ in range(n)]
t = [list(input()) for _ in range(m)]

def check(s,t,m,i,j):
    for k in range(m):
        for l in range(m):
            if s[i+k][j+l] != t[k][l]:
                return 
    return print(i+1, j+1, end="")
 
for i in range(n-m+1):
    for j in range(n-m+1):
        if s[i][j] == t[0][0]:
            check(s,t,m,i,j)