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
def dfs(cur):
    is_infec[cur] = True
    for nxt in range(n):
        if graph[cur][nxt] and not is_infec[nxt]:
            dfs(nxt)
    return

n, d = map(int, input().split())
pos = list(tuple(map(int, input().split())) for _ in range(n))

graph = [[0]*n for _ in range(n)]
for i in range(n):
    for j in range(n):
        if i == j: continue
        r = math.sqrt((pos[i][0] - pos[j][0]) ** 2 + (pos[i][1] - pos[j][1]) ** 2)
        if r <= d:
            graph[i][j] = graph[j][i] = 1

is_infec = [False]*n
is_infec[0] = True
dfs(0)

for i in range(n):
    print("Yes" if is_infec[i] else "No")