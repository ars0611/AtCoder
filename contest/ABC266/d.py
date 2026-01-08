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
n = int(input())
t = [0]
x = [0]
a = [0]
for i in range(n):
    ti, xi, ai = map(int, input().split())
    t.append(ti)
    x.append(xi)
    a.append(ai)
dp = [[-1]*5 for _ in range(n + 1)]
dp[0][0] = 0
for i in range(n):
    d = t[i + 1] - t[i]
    for j in range(5):
        if dp[i][j] == -1: continue
        for k in range(5):
            if abs(j - k) > d: continue
            if k == x[i + 1]:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j] + a[i + 1])
            else:
                dp[i + 1][k] = max(dp[i + 1][k], dp[i][j])
print(max(dp[n]))
