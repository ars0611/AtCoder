import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())

#差分をgridに
grid = [[0]*1501 for _ in range(1501)]
for i in range(n):
    a, b, c, d = map(int, input().split())
    grid[a][b] += 1
    grid[a][d] -= 1
    grid[c][b] -= 1
    grid[c][d] += 1

#横の累積和
for i in range(1501):
    for j in range(1,1501):
        grid[i][j] += grid[i][j-1]
#縦の累積和
for j in range(1501):
    for i in range(1,1501):
        grid[i][j] += grid[i-1][j]
ans = 0
for i in range(1501):
    for j in grid[i]:
        if j > 0:
            ans += 1

print(ans)

'''
A09と違い、面積を求めたので差分の置き方が少し違う。
言語化はできない
'''