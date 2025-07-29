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
n, w = map(int, input().split())
w = []
v = []
for _ in range(n):
    w_i, v_i = map(int, input().split())
    w.append(w_i) #w[i] := 品物i+1の重さ
    v.append(v_i) #v[i] := 品物i+1の価値

#DynamicProgramming
#dp[i][j] := iまでの品物をつかって得られる重さjの最大価値を格納
dp = [[0]*(w+1) for _ in range(n+1)]
for i in range(1,n+1):
    for j in range(w+1):
        