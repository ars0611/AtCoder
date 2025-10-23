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
n = int(input())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

dp = [0]*n
for i in range(n - 1):
    if i > 0 and dp[i] == 0: continue
    dp[a[i] - 1] = max(dp[a[i] - 1], dp[i] + 100)
    dp[b[i] - 1] = max(dp[b[i] - 1], dp[i] + 150)
print(dp[n - 1])