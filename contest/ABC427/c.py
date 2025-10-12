import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, m = map(int, input().split())
graph = []
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1
    v -= 1
    graph.append((u, v))
max_cnt = 0
for color in range(1 << (n - 1)):
    cnt = 0
    for u, v in graph:
        if ((color >> u) & 1) != ((color >> v) & 1):
            cnt += 1
    max_cnt = max(cnt, max_cnt)
print(m - max_cnt)