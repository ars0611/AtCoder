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
h = list(map(int, input().split()))

dp = [float("inf")] * n
dp[0] = 0
dp[1] = abs(h[1] - h[0])
for i in range(2, n):
    dp[i] = min(dp[i - 1] + abs(h[i] - h[i - 1]), dp[i - 2] + abs(h[i] - h[i - 2]))

ans = [n]
cur = n - 1
while cur != 0:
    if dp[cur] == dp[cur - 1] + abs(h[cur] - h[cur - 1]):
        cur -= 1
    else:
        cur -= 2
    ans.append(cur + 1)

k = len(ans)
ans.reverse()
print(k)
print(*ans)