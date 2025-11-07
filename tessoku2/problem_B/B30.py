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

# フェルマーの小定理を用いて,a / bの剰余を求める。
# modが素数であるときのみ用いれる。合成数ならパスカルの三角形とか使おう。
def Fermat_mod(a, b, mod):
    return ((a % mod) * power(b, mod - 2, mod)) % mod

h, w = map(int, input().split())
mod = 1000000007

n = h - 1 + w - 1
r = min(h, w) - 1

fac_n = 1
for i in range(1, n + 1):
    fac_n = fac_n * i % mod

fac_r = 1
for i in range(1, r + 1):
    fac_r = fac_r * i % mod

fac_n_r = 1
for i in range(1, n - r + 1):
    fac_n_r = fac_n_r * i % mod

denominator = fac_n
numerator = fac_r * fac_n_r % mod

print(Fermat_mod(denominator, numerator, mod))