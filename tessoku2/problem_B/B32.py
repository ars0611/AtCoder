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
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

dp = [False]*(n + 1)
for i in range(n + 1):
    if dp[i]: continue
    for j in range(k):
        if i + a[j] <= n:
            dp[i + a[j]] = True
        else:
            break

print("First" if dp[n] else "Second")