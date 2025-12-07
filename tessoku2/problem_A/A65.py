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
def dfs(curNode, curDist):
    if dist[curNode] != -1: return
    dist[curNode] = curDist
    for nxtNode in revGraph[curNode]:
        if dist[nxtNode] == -1:
            dfs(nxtNode, curDist + 1)

n = int(input())
a = list(map(int, input().split()))
revGraph = [[] for _ in range(n)]
graph = [[] for _ in range(n)]
for i in range(n - 1):
    revGraph[a[i] - 1].append(i + 1)
    graph[i + 1].append(a[i] - 1)

dist = [-1]*n
dfs(0, 0)
depth = [[] for _ in range(n)]
for i in range(n):
    depth[dist[i]].append(i)

cnt = defaultdict(int)
for i in range(n):
    for j in depth[- i - 1]:
        for k in graph[j]:
            cnt[k] += cnt[j] + 1

ans = [0]*n
for k, v in cnt.items():
    ans[k] = v
print(*ans)
