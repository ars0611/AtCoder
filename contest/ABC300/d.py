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
n = int(input())
root_n = math.isqrt(n)
# エラトステネスの篩によるroot_n以下の素数の列挙
dp = [True] * (root_n - 1)       # dp[i] := i + 2が素数かどうかをboolで持つ
for i in range(root_n - 1):      # 素数の倍数は合成数であることを利用して配るDPのイメージ
    if not dp[i]: continue
    dp[i] = True
    num = (i + 2) * 2
    while num <= root_n:
        dp[num - 2] = False
        num += i + 2

prime = []
for i in range(root_n - 1):
    if dp[i]:
        prime.append(i + 2)
m = len(prime)

cnt = 0
for i in range(m - 2):
    for j in range(i + 1, m - 1):
        a = prime[i]
        b = prime[j]
        num = math.isqrt(n // (a ** 2 * b))
        if num <= b: break
        idx = bisect.bisect_left(prime, num)
        cnt += idx - j - 1
        if idx < m and (a ** 2) * b * (prime[idx] ** 2) <= n:
            cnt += 1

print(cnt)