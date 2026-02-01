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
t = int(input())
for _ in range(t):
    n, c = map(int, input().split())
    s = [input().strip() for _ in range(n)]
    col = [SortedList() for _ in range(n)]
    for i in range(n):
        for j in range(n):
            if s[i][j] == '.':
                col[j].add(i)
    di = [-1, -1, -1]
    dj = [-1, 0, 1]
    visited = [[False] * n for _ in range(n)]
    q = deque([(n - 1, c - 1, 0, col)])
    ans = [0]*n
    while q:
        curi, curj, cnt, curcol = q.popleft()
        if cnt == n - 1:
            if curi == 0:
                ans[curj] = 1
            continue
        for k in range(3):
            ni = curi + di[k]
            nj = curj + dj[k]
            if 0 <= ni < n and 0 <= nj < n:
                if s[ni][nj] == '.':
                    q.append((ni, nj, cnt + 1, curcol))
                else:
                    idx = col[nj].bisect_left(ni + 1)
                    if idx != len(col[nj]):
                        ccol = curcol[:]
                        ccol[nj].discard(idx)
                        q.append((ni, nj, cnt + 1, ccol))
    print(*ans)
