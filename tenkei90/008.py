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
from functools import lru_cache
#----------------------------------------#
mod = 10 ** 9 + 7
n = int(input())
s = input().strip()
idx = {ch:i + 1 for i, ch in enumerate("atcoder")}
dp = [[0]*8 for _ in range(n + 1)]
dp[0][0] = 1
for i in range(n):
    for j in range(8):
        dp[i + 1][j] = dp[i][j]
        dp[i + 1][j] %= mod
    if s[i] in set("atcoder"):
        dp[i + 1][idx[s[i]]] += dp[i][idx[s[i]] - 1]
        dp[i + 1][idx[s[i]]] %= mod
print(dp[n][7] % mod)

# 耳DPって呼ばれてるらしい。
# ようは"atcoder"のうちj文字目までつくれる通り数を常態として持って、遷移し数え上げだな
# i文字目までつかって"atcoder"のj文字目まで作る組み合わせを数える
