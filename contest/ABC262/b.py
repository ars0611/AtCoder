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
n, m = map(int, input().split())
graph = [set() for _ in range(n)]
for _ in range(m):
    u, v = map(lambda x:int(x) - 1, input().split())
    graph[u].add(v)
    graph[v].add(u)
ans = 0
for a in range(n):
    for b in graph[a]:
        if a == b: continue
        for c in graph[b]:
            if b == c: continue
            if a in graph[c]:
                ans += 1
print(ans // 6)
