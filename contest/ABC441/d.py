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
from functools import lru_cache
#----------------------------------------#
n, m, l, s, t = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v, c = map(int, input().split())
    graph[u - 1].append((v - 1, c))
dp = [[[] for _ in range(n)] for _ in range(l + 1)]
dp[0][0] = [0]
for i in range(l):
    for j in range(n):
        for k in dp[i][j]:
            for nxt ,c in graph[j]:
                dp[i + 1][nxt].append(k + c)
ans = []
for j in range(n):
    for k in dp[l][j]:
        if s <= k <= t:
            ans.append(j + 1)
            break
print(*ans)
