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
n, q = map(int, input().split())
a = list(map(int, input().split()))
# ダブリング
dp = [[0]*n for _ in range(31)]     # dp[i][j] := 穴jにいるときの 2**i 日後の穴。2**30 > 10**9 から2**30日後までで十分
dp[0] = a[:]
for i in range(30):
    for j in range(n):
        cur = dp[i][j] - 1
        dp[i + 1][j] = dp[i][cur]

for _ in range(q):
    x, y = map(int, input().split())
    y_b = format(y, "b")
    # bitが立ってたら遷移
    for i in range(len(y_b)):
        if y & (1 << i):
            x = dp[i][x - 1]
    print(x)