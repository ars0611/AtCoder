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
a = list(map(int, input().split()))
seen = set()
tops = []
for cur in range(n):
    p = set()
    if cur in seen: continue
    while cur not in p and cur not in seen:
        seen.add(cur)
        p.add(cur)
        cur = a[cur] - 1
    if cur in p:
        tops.append(cur)
cycle = dict()
for top in tops:
    path = [top]
    cur = a[top] - 1
    while cur != top:
        path.append(cur)
        cur = a[cur] - 1
    cycle[top] = path
depth = [-1]*n
rev = [[] for _ in range(n)]
for i in range(n):
    rev[a[i] - 1].append(i)
par = [-1]*n
for top in tops:
    q = deque([(0, top)])
    while q:
        curd, cur = q.popleft()
        if depth[cur] != -1: continue
        depth[cur] = curd
        par[cur] = top
        for nxt in rev[cur]:
            if depth[nxt] == -1:
                q.append((curd + 1, nxt))
ans = []
for i in range(n):
    cnt = 10**100 - depth[i]
    ans.append(cycle[par[i]][cnt % len(cycle[par[i]])] + 1)
print(*ans)
