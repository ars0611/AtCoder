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
n, q = map(int, input().split())
a = list(map(lambda x: int(x) - 1, input().split()))

dp = [[i for i in range(n)] for _ in range(31)]
s = [[0] * n for _ in range(31)] 
dp[1] = a[:]
s[1] = list(range(1,n + 1))[:]
for i in range(1, 30):
    for j in range(n):
        cur = dp[i][j]
        dp[i + 1][j] = dp[i][cur]
        s[i + 1][j] = s[i][j] + s[i][cur]

for _ in range(q):
    t, b = map(int, input().split())
    cur = b - 1
    ans = 0
    t_b = format(t, "b")
    for i in range(len(t_b)):
        if t & (1 << i):
            ans += s[i + 1][cur]
            cur = dp[i + 1][cur]
    print(ans)

print(dp)
