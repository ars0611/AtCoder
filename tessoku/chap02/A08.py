import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
h, w = map(int, input().split())
x = [list(map(int, input().split())) for _ in range(h)]
q = int(input())
sum = [[0]*w for _ in  range(h)]

#行について累積和を取り、その後の列に対しても取る
for i in range(h):
    for j in range(w):
        if j == 0:
            sum[i][j] = x[i][j]
        else:
            sum[i][j] = sum[i][j-1] + x[i][j]

for j in range(w):
    for i in range(h):
        if i > 0:
            sum[i][j] += sum[i-1][j]
for _ in range(q):
    a, b, c, d = map(int, input().split())
    if a == b == 1:
        print(sum[c-1][d-1])
    elif a == 1:
        print(sum[c-1][d-1] - sum[c-1][b-2])
    elif b == 1:
        print(sum[c-1][d-1] - sum[a-2][d-1])
    else:
        print(sum[c-1][d-1] - sum[a-2][d-1] - sum[c-1][b-2] + sum[a-2][b-2])


'''
あとから気が付いたけど0行を0列を全部0にしとけば、累積和取る時も結果出力するときも条件分岐いらないですね
'''