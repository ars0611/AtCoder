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
n, k, q = map(int, input().split())
a = list(map(int, input().split()))
l = list(map(int, input().split()))

mass = [False] * n
for i in range(k):
    mass[a[i] - 1] = True
for i in range(q):
    if l[i] == n: continue
    cnt = 0
    for j in range(n):
        if mass[j]:
            cnt += 1
        if cnt == l[i]:
            idx = j
            break
    if idx + 1 == n or mass[idx + 1]: continue
    mass[idx] = False
    mass[idx + 1] = True
ans = []
for i in range(n):
    if not mass[i]: continue
    ans.append(i + 1)
print(*ans)
