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
n, x = map(int, input().split())
wallet = sorted([tuple(map(int, input().split())) for _ in range(n)])
a = [wallet[i][0] for i in range(n)]
b = [wallet[i][1] for i in range(n)]
dp = [[False]*(x + 1) for _ in range(n + 1)]
dp[0][0] = True
for i in range(1, n + 1):
    for j in range(x + 1):
        if dp[i - 1][j]:
            dp[i][j] = True
            for k in range(b[i - 1] + 1):
                if x >= j + a[i - 1] * k:
                    dp[i][j + a[i - 1] * k] = True
print("Yes" if dp[n][x] else "No")
