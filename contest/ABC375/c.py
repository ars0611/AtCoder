import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
grid = []
for i in range(n):
    a_i = list(input())
    grid.append(a_i)
ans = [["None"]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        
        d = min(i + 1, j + 1, n - i, n - j)
        cur_x = i
        cur_y = j
        
        for k in range(d % 4):
            next_x = cur_y 
            next_y = n - 1 - cur_x
            cur_x = next_x
            cur_y = next_y
        ans[cur_x][cur_y] = grid[i][j]

for i in range(n):
    print("".join(ans[i]))

#解説AC
#考察しきれるわけがない