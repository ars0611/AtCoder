import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
h,w,n = map(int, input().split())
s = [[0]*(w+2) for _ in range(h+2)]
#差分を入力
for _ in range(n):
    a, b, c, d = map(int, input().split())
    s[a][b] += 1
    s[a][d+1] -= 1
    s[c+1][b] -= 1
    s[c+1][d+1] += 1

#横の累積和をとる
for i in range(1,h+1):
    for j in range(1,w+1):
        s[i][j] += s[i][j-1]
#縦の累積和をとる
for j in range(1,w+1):
    for i in range(1,h+1):
        s[i][j] += s[i-1][j]

for i in range(1,h+1):
    for j in range(1,w+1):
        if j == w:
            print(s[i][j])
            break
        print(s[i][j],end=" ")