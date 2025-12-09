import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
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
# エラトステネスの篩によるn以下の素数の列挙
n = 3 * 10**6
dp = [True]* (n - 1)       # dp[i] := i + 2が素数かどうかをboolで持つ
for i in range(n - 1):      # 素数の倍数は合成数であることを利用して配るDPのイメージ
    if not dp[i]: continue
    dp[i] = True
    num = (i + 2) * 2
    while num <= n:
        dp[num - 2] = False
        num += i + 2

prime = []
for i in range(n - 1):
    if dp[i]:
        prime.append(i + 2)
primeSet = set(prime)

t = int(input())
for _ in range(t):
    num = int(input())
    for m in prime:
        if num % m != 0: continue
        p = m if num % m ** 2 == 0 else math.isqrt(num // m)
        q = num // m ** 2 if num % m ** 2 == 0 else m
        print(p, q)
        break

# 2 <= p <= sqrt(n)は思ったが、上からの評価が甘く、pで全探索はできなかった。
# ↑これがわかるなら、qは pow(n, 1 / 3) <= q <= n // 4 と思いつくべきだった。
# そしたら自然に min(p, q) =< n**(1 / 3) に気付けた。頭が悪すぎる。
# 素数p, qであることが問題文でわかっているから片方決め打ちできたらもう片方は素数で確定できる。
