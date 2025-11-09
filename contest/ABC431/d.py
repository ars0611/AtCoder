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
n = int(input())
w = []
h = []
b = []
for i in range(n):
    wi, hi, bi = map(int, input().split())
    w.append(wi)
    h.append(hi)
    b.append(bi)

s = sum(w)
dp = [[0]*(s // 2 + 1) for _ in range(n + 1)]
for i in range(n):
    for j in range(s // 2 + 1):
        if j - w[i] >= 0:
            dp[i + 1][j] = max(dp[i][j - w[i]] + h[i], dp[i][j] + b[i])
        else:
            dp[i + 1][j] = dp[i][j] + b[i]
        

ans = 0
for j in range(s // 2 + 1):
    ans = max(ans, dp[n][j])

print(ans)