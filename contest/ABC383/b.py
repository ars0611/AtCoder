import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
h, w, d = map(int, input().split())
grid = []
for _ in range(h):
    s_i = list(input())
    grid.append(s_i)

floor = []
for i in range(h):
    for j in range(w):
        if grid[i][j] == ".":
            floor.append([i,j])
c = list(itertools.combinations(floor, 2))

grid_copy = copy.deepcopy(grid)
ans = 0
for c_i in c:
    
    c_i = list(c_i)
    i_1 = c_i[0][0]
    j_1 = c_i[0][1]
    i_2 = c_i[1][0]
    j_2 = c_i[1][1]
    cnt = 0
    
    for d_i in range(-d,d+1):
        for d_j in range(-d,d+1):
            if abs(d_i) + abs(d_j) <= d and 0 <= i_1 + d_i <= h - 1 and 0 <= j_1 + d_j <= w - 1 and grid_copy[i_1 + d_i][j_1 + d_j] == ".":
                cnt += 1    
                grid_copy[i_1 + d_i][j_1 + d_j] = "#"
            if abs(d_i) + abs(d_j) <= d and 0 <= i_2 + d_i <= h - 1 and 0 <= j_2 + d_j <= w - 1 and grid_copy[i_2 + d_i][j_2 + d_j] == ".":
                cnt += 1    
                grid_copy[i_2 + d_i][j_2 + d_j] = "#"
    ans = max(cnt, ans)
    grid_copy = copy.deepcopy(grid)
print(ans)