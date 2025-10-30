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

dp = [0] * n
l = [max(a) + 1] * n
dp[0] = 1
l[0] = a[0]

ans = dp[0]
for i in range(1, n):
    idx = bisect.bisect_left(l, a[i])
    dp[i] = idx + 1
    l[idx] = min(l[idx], a[i])
    ans = max(ans, dp[i])

print(ans)