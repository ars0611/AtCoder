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
n, k = map(int, input().split())

#dp[i][j] := 数字jに対し,操作を2**i回行った後の数字
#k <= 10**9 < 2**30より,i <= 29としてよい
dp = [[0]* (n+1) for _ in range(30)]

#1行目はそれぞれに対し,各桁の和を一度引くだけなので自明に求まる
for j in range(1, n+1):
    w = j
    n_j = 0
    while j != 0:
        n_j += j % 10
        j //= 10
    dp[0][w] = w - n_j

#操作を2**i回行った結果は2**(i-1)回行った結果にさらに2**(i-1)回操作を行うことで求まる
for i in range(1, 30):
    for j in range(n+1):
        dp[i][j] = dp[i-1][dp[i-1][j]]

#操作回数を二進変換してビットが立ってたらそこの重み回数だけ操作を行う
for i in range(1,n+1):
    for j in range(29, -1, -1):
        if (k >> j & 1 == 1):
            i = dp[j][i]
    print(i)