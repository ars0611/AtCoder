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
s = input().strip()
n = len(s)
mod = 998244353

dp = [[0]*(n + 1) for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(n):
        if s[i] != ")":
            dp[i + 1][j + 1] += dp[i][j]
        if j != 0 and s[i] != "(":
            dp[i + 1][j - 1] += dp[i][j]

print(dp[n][0] % mod)

# かっこ列の性質として、任意のi文字目までで"("の数の方が")"の数より多いというものがある。なのでこれを利用して"?"の置き換えを左から順に考えれる。
# "("の数が重要であることを認識できていれば、?の置き換えは左から順に決まることが容易にわかり、そこから漸化的に解けることがわかり、DPにたどり着くのか。
# 制約からn*nのdpなのは察してたけど、状態をどうとればいいかわかんなかったな。
# かっこ列の性質を知らなかったからといえばそれまでだけど、0から発想できそうでもある。