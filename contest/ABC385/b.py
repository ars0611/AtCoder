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
h, w, x, y = map(int, input().split())
grid = []
for _ in range(h):
    s_i = list(input())
    grid.append(s_i)
t = input()

cnt  = 0
visited = set()
cur_i = x-1
cur_j = y-1
for i in range(len(t)):
    
    if t[i] == "U" and grid[cur_i-1][cur_j] != "#":
        cur_i -= 1
    elif t[i] == "D" and grid[cur_i+1][cur_j] != "#":
        cur_i += 1
    elif t[i] == "L" and grid[cur_i][cur_j-1] != "#":
        cur_j -= 1
    elif t[i] == "R" and grid[cur_i][cur_j+1] != "#":
        cur_j += 1
    
    if grid[cur_i][cur_j] == "@" and not (cur_i, cur_j) in visited:
        cnt += 1
        visited.add((cur_i, cur_j))
print(cur_i+1, cur_j+1, cnt, end=" ")