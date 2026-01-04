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
n = int(input())
p = list(map(int, input().split()))
q = []
for i in range(n):
    q.append((p[i] - i - 1) % n)
    q.append((p[i] - i + 1) % n)
    q.append((p[i] - i) % n)
qc = Counter(q)
ans = 0
for i in range(n):
    ans = max(ans, qc[i])
print(ans)

# これ面白かった。各料理が何周したら喜ばせられるかを記録して、最も多い周数の数を数えればよい。
# 各料理で何周するべきかのパートは必ず3種かぶらずに求まる

