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
h, w = map(int, input().split())
mod = 10**9 + 7

#右に進むこととと下に進むことの並び替えと捉えられる（懐かしい）のでnCrを用いる
#階乗計算
n = h+w-2
r = w-1

n_fac = 1
r_fac = 1
nr_fac = 1

for i in range(1,n+1):
    
    n_fac = (n_fac * i) % mod
    
    if i <= r:
        r_fac = (r_fac * i) % mod

    if i <= n-r :
        nr_fac = (nr_fac * i) % mod

a = n_fac #分子
b = r_fac * nr_fac #分母
#フェルマーの小定理からmod(a/b) == mod(a*b**(mod-2))
#b**(mod - 2)を繰り返し二乗法で求める
m = mod - 2 #指数
res = 1
while m > 0:
    if m % 2 == 1:
        res = (res * b) % mod
    b = (b*b) % mod
    m //= 2
b = res

ans = (a*b)%mod
#出力
print(ans)
