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
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    graph[u].append(v)
    graph[v].append(u)
s = input().strip()

q = deque()
for i in range(n):
    if s[i] == "S":
        q.append((i, i, 0))

dist = [0]*n
starts = [set() for _ in range(n)]
while q:
    start, cur, d = q.popleft()
    if start in starts[cur] or len(starts[cur]) >= 2: continue
    dist[cur] += d
    starts[cur].add(start)
    for nxt in graph[cur]:
        if not start in starts[nxt] and len(starts[nxt]) < 2:
            q.append((start, nxt, d + 1))

for i in range(n):
    if s[i] == "D":
        print(dist[i])