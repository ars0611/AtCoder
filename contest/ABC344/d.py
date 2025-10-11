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
t = input().strip()
n = int(input())
dp = [[float("inf")] * (len(t) + 1) for _ in range(n + 1)]
dp[0][0] = 0
for i in range(1, n + 1):
    bag = list(input().split())
    a = int(bag[0])
    for j in range(a):
        s = bag[1 + j].strip()
        for k in range(len(t) + 1):
            if k + len(s) <= len(t) and t[:k] + s == t[:k+len(s)]:
                dp[i][k + len(s)] = min(dp[i - 1][k + len(s)], dp[i - 1][k] + 1, dp[i][k + len(s)])
            dp[i][k] = min(dp[i - 1][k], dp[i][k])
print(dp[n][len(t)] if dp[n][len(t)] != float("inf") else -1)
print(dp)