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
box = []
for _ in range(n):
    x, y = map(int, input().split())
    box.append((x, y))
print(box)
box.sort(key = lambda x:(x[0], -x[1]))
print(box)
l = [500001] * n
dp = [0] * n
l[0] = box[0][1]
dp[0] = 1

ans = 1
for i in range(1, n):
    y = box[i][1]
    idx = bisect.bisect_left(l, y)
    dp[i] = idx + 1
    l[idx] = min(l[idx], y)
    ans = max(ans, dp[i])
print(ans)