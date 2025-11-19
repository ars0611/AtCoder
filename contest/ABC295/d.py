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
s = input().strip()
n = len(s)

pre_sum = [[0] for _ in range(10)] # pre_sum[i][j] := j文字目までにiが登場した回数のmod2
for i in range(n):
    for j in range(10):
        if int(s[i]) == j:
            pre_sum[j].append((pre_sum[j][-1] + 1) % 2)
        else:
            pre_sum[j].append(pre_sum[j][-1])

c = defaultdict(int)
for i in range(n + 1):
    bit = 0
    for j in range(10):
        bit += pre_sum[j][i]
        if j < 9:
            bit *= 10
    c[bit] += 1

ans = 0
for cnt in c.values():
    ans += (cnt * (cnt - 1)) // 2

print(ans)

# まじであと一歩だった。i文字目までのx(0 <= x < 10)の登場回数の累積和をとった
# 左端固定で右端決める際に、すべてのxの登場回数が偶数階であればよいことは気づいた
# ただ、二分探索などで高速に求められないから困っていた
# 偶奇に着目すればよいので、累積和をすべてmod2で管理
# mod2なのでビットで管理して、10bitの情報が等しいもののペアがうれしい列 <- ここが大事