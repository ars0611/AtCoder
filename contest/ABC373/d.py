import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
#始点を1にしてしまおう
n, m = map(int, input().split())

node = [[] for _ in range(n)]
visited = [False]*n
n_num  = [0]*n
for i in range(m):
    u, v, w = map(int, input().split())
    u -= 1
    v -= 1
    node[u].append((v, w))
    node[v].append((u, -w))

for i in range(n):
    
    if visited[i]:
        continue
    
    n_num[i] = 0
    queue = deque([i])
    visited[i] = True
    while queue:
        cur = queue.popleft()
        for next in node[cur]:
            if not visited[next[0]]:
                visited[next[0]] = True
                n_num[next[0]] = n_num[cur] + next[1]
                queue.append(next[0])

print(*n_num)

