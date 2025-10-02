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
dp = [[1]*n for _ in range(2) ] #dp[0][j] := 手前からj番目を頂点に据えた際のサイズ, [1][j]はうしろから
dp[0][0] = 1
dp[1][-1] = 1

for i in range(1,n):
    if a[i] > dp[0][i-1]:
        dp[0][i] = dp[0][i-1] + 1
    else:
        dp[0][i] = a[i]
    if a[-1-i] > dp[1][-1-i+1]:
        dp[1][-i-1] = dp[1][-i-1+1] + 1
    else:
        dp[1][-i-1] = a[-i-1]
ans = 1
for i in range(n):
    ans = max(ans, min(dp[0][i], dp[1][i]))
print(ans)