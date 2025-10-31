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
dp = [True]*n

for i in range(n - 1):
    if not dp[i]: continue
    dp[i] = True
    num = (i + 2) * 2
    while num <= n:
        dp[num - 2] = False
        num += i + 2

for i in range(n - 1):
    if dp[i]: print(i + 2)