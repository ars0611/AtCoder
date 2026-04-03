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
def dfs(curi, curj, cnt):
    if visited[curi][curj] != -1: return
    visited[curi][curj] = cnt
    nxti = curi + 1
    nxtj = curj + 1
    if nxtj < w and grid[curi][nxtj] == '.' and visited[curi][nxtj] == -1:
        dfs(curi, nxtj, cnt + 1)
    if nxti < h and grid[nxti][curj] == '.' and visited[nxti][curj] == -1: 
        dfs(nxti, curj, cnt + 1)
h, w = map(int, input().split())
grid = [input().strip() for _ in range(h)]
visited = [[-1]*w for _ in range(h)]
dfs(0, 0, 1)
ans = 0
for i in range(h):
    for j in range(w):
        ans = max(ans, visited[i][j])
print(ans)
