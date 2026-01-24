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
mon = []
for i in range(n):
    x, y = map(int, input().split())
    if x == 0:
        if y > 0:
            inc = 10 ** 10 * 1.0
        else:
            inc = -10 ** 10 * 1.0
    else:
        inc = y / x
    g = math.gcd(abs(x), abs(y))
    mon.append((inc, y, x, i, g))
mon.sort(reverse=True)
query = [tuple(map(lambda x:int(x) - 1, input().split())) for _ in range(q)]
zipped = dict()
preSum = [0]
incs = []
idx = 0
for i in range(n):
    inc, y, x, num, g = mon[i]
    if inc >= 0.0 and y >= 0 and x >= 0:
        if incs and incs[-1][0] == inc and x / g == incs[-1][1] and y / g == incs[-1][2]:
            zipped[num] = idx - 1
            preSum[-1] += 1
        else:
            zipped[num] = idx
            preSum.append(preSum[-1] + 1)
            idx += 1
        incs.append((inc, x / g, y / g))
for i in range(n):
    inc, y, x, num, g = mon[i]
    if inc < 0.0 and y < 0 and x >= 0:
        if incs and incs[-1][0] == inc and x / g == incs[-1][1] and y / g == incs[-1][2]:
            zipped[num] = idx - 1
            preSum[-1] += 1
        else:
            zipped[num] = idx
            preSum.append(preSum[-1] + 1)
            idx += 1
        incs.append((inc, x / g, y / g))
for i in range(n):
    inc, y, x, num, g = mon[i]
    if inc > 0.0 and y < 0 and x <= 0:
        if incs and incs[-1][0] == inc and x / g == incs[-1][1] and y / g == incs[-1][2]:
            zipped[num] = idx - 1
            preSum[-1] += 1
        else:
            zipped[num] = idx
            preSum.append(preSum[-1] + 1)
            idx += 1
        incs.append((inc, x / g, y / g))
for i in range(n):
    inc, y, x, num, g = mon[i]
    if inc <= 0.0 and y >= 0 and x <= 0:
        if incs and incs[-1][0] == inc and x / g == incs[-1][1] and y / g == incs[-1][2]:
            zipped[num] = idx - 1
            preSum[-1] += 1
        else:
            zipped[num] = idx
            preSum.append(preSum[-1] + 1)
            idx += 1
        incs.append((inc, x / g, y / g))
for a, b in query:
    idxA = zipped[a]
    idxB = zipped[b]
    if idxB >= idxA:
        ans = preSum[idxB + 1] - preSum[idxA]
    else:
        ans = preSum[-1] - preSum[idxA] + preSum[idxB + 1]
    print(ans)

