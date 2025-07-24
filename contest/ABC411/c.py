import sys
sys.setrecursionlimit(10*6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
N,Q = map(int, input().split())
A = list(map(int, input().split()))

#白のマスを0,黒を1とする
B =[0]*(N+2)

#塗り替えたマスの両隣の色に応じて、連続する部分が増減する
ans = 0
for i in A:
    B[i] = (B[i] + 1) % 2
    if B[i] == 0:
        if B[i-1] == B[i+1] == 1:
            ans += 1
        elif B[i-1] == B[i+1] == 0:
            ans -= 1
    else:
        if B[i-1] == B[i+1] == 1:
            ans -= 1
        elif B[i-1] == B[i+1] == 0:
            ans += 1
    print(ans)