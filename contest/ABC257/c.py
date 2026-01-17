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
s = input().strip()
w = list(map(int, input().split()))
p = []
for i in range(n):
    p.append((w[i], int(s[i])))
p.sort()
preSumAd = [0]
for i in range(n):
    if p[i][1] == 0:
        preSumAd.append(preSumAd[-1])
    else:
        preSumAd.append(preSumAd[-1] + 1)
ans = 0
seen = set()
for i in range(1, n + 1):
    if p[i - 1][0] in seen: continue
    ans = max(ans, preSumAd[n] - preSumAd[i - 1] + (i - 1) - preSumAd[i - 1])
    seen.add(p[i - 1][0])
ans = max(ans, n - preSumAd[n])
print(ans)
