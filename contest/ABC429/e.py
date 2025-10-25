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
def dfs(cur, safe, dist):
    if cur in seen:
        return
    seen.add(cur)
    for nxt in graph[cur]:
        if nxt not in seen:
            if not is_safe[nxt]:
                dists[nxt].add(dist + 1)
            dfs(nxt, is_safe[nxt], dist + 1)
    return

n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    u, v = map(int, input().split())
    u -= 1; v -= 1
    graph[u].append(v)
    graph[v].append(u)
s = input().strip()

start = []
is_safe = [False]*n
for i in range(n):
    if s[i] == "S":
        is_safe[i] = True
        start.append(i)
    else:
        is_safe[i] = False

dists = [SortedList() for _ in range(n)]
for node in start:
    seen = set()
    dfs(node, True, 0)

for i in range(n):
    if not is_safe[i]:
        print(dists[i][0] + dists[i][1])
print(dists)