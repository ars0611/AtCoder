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
from functools import cmp_to_key
#----------------------------------------#
n, k = map(int, input().split())
arr = [list(map(int, input().split())) for _ in range(2)]
dp = [[False]*2 for _ in range(n)]
dp[0] = [True]*2
for i in range(n - 1):
    for j in range(2):
        if not dp[i][j]: continue
        for l in range(2):
            if abs(arr[j][i] - arr[l][i + 1]) <= k:
                dp[i + 1][l] = True
print("Yes" if dp[n - 1][0] or dp[n - 1][1] else "No")

# 一個前の結果で決まることが問題文から明らかなので動的計画法
