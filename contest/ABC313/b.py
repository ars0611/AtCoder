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
def dfs(cur):
    if visited[cur]: return
    visited[cur] = True
    for nxt in rel[cur]:
        if not visited[nxt]:
            dfs(nxt)

n, m = map(int, input().split())
rel = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int, input().split())
    a -= 1; b -= 1
    rel[a].append(b)

for i in range(n):
    visited = [False]*n
    dfs(i)
    if visited == [True]*n:
        print(i + 1)
        break
else:
    print(-1)