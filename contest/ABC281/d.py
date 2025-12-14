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

dp = [[-1]*(d) for _ in range(k + 1)]
dp[0][0] = 0

for ai in a:
    for i in range(k - 1, -1, -1):
        for j in range(d):
            if dp[i][j] == -1: continue
            dp[i + 1][(j + ai) % d] = max(dp[i + 1][(j + ai) % d], dp[i][j] + ai)

print(dp[k][0])

# bit全探索で考えるとO(n*2**k)
# これをO(n*k)に落とすのがナップサックだし、部分和典型でもある
# iを昇順で見ると、ai使って遷移した先でまたaiをつかってしまうので、降順に見る
