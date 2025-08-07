import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
#入力
n, r =map(int, input().split())
mod = 10**9 + 7

#階乗計算
n_fac = 1
r_fac = 1
n_r_fac = 1
for i in range(1,n+1):
    n_fac = n_fac * i % mod
    if i <= r:
        r_fac = r_fac * i % mod
    if i <= n-r:
        n_r_fac = n_r_fac * i % mod

a = n_fac #分子
b = r_fac * n_r_fac #分母

#a/bを素数mで割ったときの余りはa * (b**(m-2))をmで割ったときの余りと等しいらしい(証明略)
#b ** (mod-2)を繰り返し二乗法で求める
m = mod-2
res = 1
while m > 0:
    #指数を二進変換して、ビットが立っている箇所のみ累乗項をかけていく
    if m % 2 == 1:
        res = res * b % mod
    b = b * b % mod
    m //= 2
b = res


#出力
print((a*b)%mod)