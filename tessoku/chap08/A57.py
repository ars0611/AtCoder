import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy
from sortedcontainers import SortedSet, SortedList, SortedDict

#----------------------------------------#
n, q = map(int, input().split())
a = list(map(int, input().split()))

#dp[h][w] := 穴w-1にいて,2**h日後にいる穴を表す
#y_j < 2**30より,h <= 29としてよい
dp = [[0] * n for _ in range(30)]
dp[0] = a[:]
for i in range(1, 30):
    for j in range(n):
        dp[i][j] = dp[i-1][dp[i-1][j] - 1]

#クエリ処理
for i in range(q):
    x, y = map(int, input().split())
    for j in range(29,-1,-1):
        if y >> j & 1 == 1:
            x = dp[j][x-1]
    print(x)
