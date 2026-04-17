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
n = int(input())
t = []
k = []
a = []
for _ in range(n):
    _t, _k, *_a = map(int, input().split())
    t.append(_t)
    k.append(_k)
    a.append(_a)
needA = set([n - 1])
stack = [n - 1]
while stack:
    cur = stack.pop()
    for nxt in a[cur]:
        if nxt not in needA:
            stack.append(nxt - 1)
        needA.add(nxt - 1)
needA = sorted(list(needA))
ans = [0]*n
for ai in needA:
    c = 0
    for j in range(k[ai]):
        c += ans[a[ai][j] - 1]
    ans[ai] = c + t[ai]
print(ans[n - 1])
