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
#----------------------------------------#
n, m = map(int, input().split())
graph = [[(i + n) % (2 * n)] for i in range(2 * n)]
for _ in range(m):
    a, b, c, d = input().split()
    a = int(a) - 1
    c = int(c) - 1
    if b == "B":
        a += n
    if d == "B":
        c += n
    graph[a].append(c)
    graph[c].append(a)
x = 0
y = 0
visited = [False]*2 * n
for i in range(n):
    if visited[i]: continue
    q = deque([i])
    while q:
        cur = q.popleft()
        if visited[cur]:
            x += 1
            break
        visited[cur] = True
        for nxt in graph[cur]:
            if not visited[nxt]:
                q.append(nxt)
            
    else:
        y += 1
print(x, y)