import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n = int(input())
p = []
for i in range(n - 1):
    d = list(map(int, input().split()))
    p.append(d)
dp = [0]*(1 << n)
for bit in range((1 << n) - 1):
    l = -1
    for i in range(n):
        if not(bit >> i & 1):
            l = i
            break
    for i in range(l + 1, n):
        if not(bit >> i & 1):
            nxt = bit | (1 << l) | (1 << i)
            dp[nxt] = max(dp[nxt], dp[bit] + p[l][i - l - 1])
print(dp[-1])

# bitDPを本格的に学ばないといけなくなってきた。
# 使った頂点の集合をbitで管理し、配るDPのイメージかな
# ビットシフト絡むと頭爆発するわ。辺の重みの配列もきもいしさあ