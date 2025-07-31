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
#入力
h, w = map(int, input().split())
s = []
for _ in range(h):
    s.append(list(input()))

#a,b,c,d初期化
a = h-1
b = 0
c = w-1
d = 0

#a,b,c,dを決定
for i in range(h):
    for j in range(w):
        if s[i][j] == "#":
            a = min(a, i)
            b = max(b,i)
            c = min(c,j)
            d = max(d,j)

#長方形a,b,c,dの中に"."が含まれていたら長方形を作れない
for i in range(a,b+1):
    for j in range(c,d+1):
        if s[i][j] == ".":
            print("No")
            exit()
print("Yes")