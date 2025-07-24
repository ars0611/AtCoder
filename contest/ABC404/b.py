import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N = int(input())
S = [list(input()) for i in range(N)]
T = [list(input()) for i in range(N)]


def rotate(grid):
    rotated_grid = [[None]*N for _ in range(N)]
    for j in range(N):
        for k in range(N):
            rotated_grid[k][-j-1] = grid[j][k]
    return rotated_grid

ans = N**2

for i in range(4):
    rotate_cnt = i
    cnt = 0
    for j in range(N):
        for k in range(N):
            if T[j][k] != S[j][k]:
                cnt += 1
    ans = min(ans, cnt + rotate_cnt)
    S = rotate(S)
print(ans)