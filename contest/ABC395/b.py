import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict

#----------------------------------------#
n = int(input())
grid = [[None]*n for _ in range(n)]

for i in range(n):
    if i < n-i:
        for j in range(i,n-i):
            for k in range(i,n-i):
                if i % 2 == 0:
                    grid[j][k] = "#"
                else:
                    grid[j][k] = "."

for i in range(n):
    print("".join(grid[i]))

#ネストが深すぎやしませんか