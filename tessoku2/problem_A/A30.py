import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations

#----------------------------------------#
# 繰り返し二乗法による累乗の剰余計算 <- しょーみpow(a, b, mod)で良い
def power(a, b, mod):
    # 指数を2進変換した際のビット数を求める。
    k = 0
    while 1 << k <= b:
        k += 1

    # 繰り返し二乗法
    res = 1
    p = a
    for i in range(k):
        if (1 << i) & b:
            res = (res * p) % mod
        p = (p * p) % mod
    
    return res

n, r = map(int, input().split())
mod = 1000000007

fac_n = 1
fac_r = 1
fac_n_minus_r = 1
for i in range(n, 0, -1):
    fac_n *= i
    fac_n %= mod

    if r >= i:
        fac_r *= i
        fac_r %= mod

    if n - r >= i:
        fac_n_minus_r *= i
        fac_n_minus_r %= mod

denominator = fac_n                                         # 分母
numerator = (fac_r * fac_n_minus_r) % mod                   # 分子
ans = (denominator * power(numerator, mod - 2, mod)) % mod  # フェルマーの小定理より

print(ans)