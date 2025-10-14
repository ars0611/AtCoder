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
s = input().strip()
t = input().strip()
dp = [[0] * (len(t) + 1) for _ in range(len(s) + 1)]
for i in range(1, len(s) + 1):
    for j in range(len(t) + 1):
        if j == 0:
            dp[i][j] =dp[i - 1][j]
            continue
        if s[i - 1] == t[j - 1]:
            dp[i][j] = max(dp[i][j], dp[i][j - 1], dp[i - 1][j - 1] + 1)
        else:
            dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])
print(dp[-1][-1])