import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
n = int(input())

#まずは与えられた点の座標を打つ
# x,yの制約から1502が出てきてます
grid = [[0]*1502 for _ in range(1502)]
for _ in range(n):
    x, y = map(int, input().split())
    grid[x][y] += 1

#点の個数の累積和を取る
#まずはx軸方向の累積和
for i in range(1,1502):
    for j in range(1,1502):
        grid[i][j] += grid[i][j-1]

#次にy軸方向の累積和
for j in range(1,1502):
    for i in range(1,1502):
        grid[i][j] += grid[i-1][j]

q = int(input())
for _ in range(q):
    a,b,c,d = map(int, input().split())
    print(grid[c][d] - grid[c][b-1] - grid[a-1][d] + grid[a-1][b-1])

#i!=j で (x_i,y_i) == (x_j,y_j) きたとき新しい点として数えるの納得いかない