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
n, s = map(int, input().split())
cards = [tuple(map(int, input().split())) for _ in range(n)]
dp = [[False]*(10001) for _ in range(n + 1)]
dp[0][0] = True
for i in range(n):
    a, b = cards[i]
    for j in range(s + 1):
        if not dp[i][j]: continue
        dp[i + 1][j + a] = True
        dp[i + 1][j + b] = True
dir = []
cur = s
for i in range(n):
    a, b = cards[n - i - 1]
    if dp[n - i - 1][cur - a]:
        dir.append("H")
        cur -= a
    elif dp[n - i - 1][cur - b]:
        dir.append("T")
        cur -= b
    else:
        print("No")
        break
else:
    print("Yes")
    print("".join(reversed(dir)))
