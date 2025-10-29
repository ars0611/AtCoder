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
def move(prev, cur):
    return (math.sqrt((pos_x[prev] - pos_x[cur]) ** 2 + (pos_y[prev] - pos_y[cur]) ** 2))

n = int(input())
pos_x = []
pos_y = []
for i in range(n):
    x, y = map(int, input().split())
    pos_x.append(x)
    pos_y.append(y)

dp = [([float(10**9)]*(1 << n)) for _ in range(n)]
dp[0][0] = float(0)
for j in range((1 << n)):
    for i in range(n):
        if dp[i][j] == float(10**9): continue
        for k in range(n):
            if j & (1 << k): continue
            dp[k][(j | (1 << k))] = min(dp[k][(j | (1 << k))], dp[i][j] + move(i, k))

print(dp[0][(1 << n) - 1])