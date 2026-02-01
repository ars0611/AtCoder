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
t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    s = [input().strip() for _ in range(n)]
    dp = [[False]*n for _ in range(n)]
    dp[n - 1][c - 1] = True
    l = [n - 1]*n
    for i in range(n):
        dp[i][c - 1] = True
        for j in range(n):
            if s[i][j] == '#':
                l[j] = i
    for i in range(n - 2, -1, -1):
        for j in range(n):
            if j > 0 and dp[i + 1][j - 1] or j + 1 < n and dp[i + 1][j + 1] or dp[i + 1][j]:
                if s[i][j] == '.':
                    dp[i][j] = True
                elif l[j] == i:
                    for ii in range(i + 1):
                        dp[ii][j] = True
    ans = ['0']*n
    for j in range(n):
        if dp[0][j]:
            ans[j] = '1'
    print("".join(ans))

# 一番下から上に向かうのでbfsではなく下からのdpを考える
# 自分がいる場所より下すべてが.であるとき、そこより真上は直進で壁を破壊できる
# なので列ごとに最も下にある壁を持っておけば、その最も下の壁に到達したとき、直進で(0, j)が到達可能になる
