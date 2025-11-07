import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
n, a, b = map(int, input().split())

dp = [False]*(n + 1) # Falseは負けう
for i in range(n + 1):
    if dp[i]: continue
    if i + a <= n:
        dp[i + a] = not dp[i]
    if i + b <= n:
        dp[i + b] = not dp[i]

print("First" if dp[n] else "Second")