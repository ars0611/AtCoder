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
n, k, d = map(int, input().split())
a = list(map(int, input().split()))

dp = [[-1]*(d + 1) for _ in range(k + 1)]
used = [[set() for _ in range(d + 1)] for _ in range(k + 1)]
dp[0][0] = 0
for i in range(k):
    for j in range(d + 1):
        if dp[i][j] == -1: continue
        for k in range(n):
            
