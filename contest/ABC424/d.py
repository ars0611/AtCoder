import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
t = int(input())
dx = [0,1,1,1,0,-1,-1,-1]
dy = [1,1,0,-1,-1,-1,0,1]
for _ in range(t):
    h,w = map(int, input().split())
    grid = [list(input().strip()) for _ in range(h)]
    block = [[0]*w for _ in range(h)]
    ans = 0
    for i in range(h-1):
        for j in range(w-1):
            if grid[i][j] == '#' and grid[i+1][j] == '#' and grid[i][j+1] == '#' and grid[i+1][j+1] == '#':
                block[i][j] += 1
                block[i+1][j] += 1
                block[i][j+1] += 1
                block[i+1][j+1] += 1
    for i in range(h):
        for j in range(w):
            if block[i][j] == 0:
                continue
            
            m = 0
            idx = (i,j)
            for di in range(2):
                for dj in range(2):
                    ni = i + di
                    nj = j + dj
                    if 0 <= ni < h and 0 <= nj < w and block[ni][nj] > m:
                        m = block[ni][nj]
                        idx = (ni,nj)
            
            block[idx[0]][idx[1]] = 0
            ans += 1
            
            for di in range(8):
                for dj in range(8):
                    ni = idx[0] + dx[di]
                    nj = idx[1] + dy[dj]
                    if 0 <= ni < h and 0 <= nj < w:
                        block[ni][nj] = 0
    print(ans)

# 想定嘘の嘘貪欲を踏んだ
# Todo: BitDP履修