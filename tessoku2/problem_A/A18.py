import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, s = map(int, input().split())
a = list(map(int, input().split()))

dp = [[False] * (s + 1) for _ in range(n + 1)]  # カードiまでで和jを作れるかboolで持つ
dp[0][0] = True                                 #カードを使わずとも0は作れる
for i in range(1, n + 1):
    for j in range(s + 1):
        if dp[i - 1][j]:                        # カードi - 1までで和jを作れるならカードiまででも作れる
            dp[i][j] = True
        else:
            if a[i - 1] > j: continue               # カードiを用いて作れる和は小さくともa[i]以上
            if dp[i - 1][j - a[i - 1]]:             # j - a[i]をカードi - 1までで作れるならカードiを用いて和jを作れる
                dp[i][j] = True

print("Yes" if dp[n][s] else "No")