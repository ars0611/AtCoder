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
n, k = map(int, input().split())
a = [i for i in range(n + 1)]
for i in range(n + 1):
    d = 0
    num = i
    while num > 0:
        d += num % 10
        num //= 10
    a[i] -= d

# ダブリング
dp = [[0]*(n + 1) for _ in range(31)] # dp[i][j] = j に2**i回操作をしたときの値。2**30までで十分。
dp[0] = a[:]
for i in range(30):
    for j in range(n + 1):
        dp[i + 1][j] = dp[i][dp[i][j]]


for j in range(1, n + 1):
    k_b = format(k, "b")
    for i in range(len(k_b)):
        if k & (1 << i):
            j = dp[i][j]
    print(j)
