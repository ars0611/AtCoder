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
from functools import cmp_to_key
#----------------------------------------#
m, a, b = map(int, input().split())
flgs = [[False]*m for _ in range(m)]
seen = set()
for i in range(m):
    flgs[0][i] = flgs[i][0] = True
    seen.add((0, i))
    seen.add((i, 0))
for i in range(m):
    for j in range(m):
        if (i, j) in seen: continue
        stack = [(i, j)]
        s = [i, j]
        flg = False
        while True:
            if (s[-2], s[-1]) in seen:
                flg = flgs[s[-2]][s[-1]]
                break
            if s[-1] == 0:
                flg = True
                break
            stack.append((s[-2], s[-1]))
            seen.add((s[-2], s[-1]))
            s.append((a * s[-1] + b * s[-2]) % m)
        while stack:
            i, j = stack.pop()
            flgs[i][j] = flg
cnt = 0
for i in range(m):
    for j in range(m):
        if not flgs[i][j]:
            cnt += 1
print(cnt)
