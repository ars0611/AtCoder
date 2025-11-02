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
grid = [list(input().strip()) for _ in range(n)]

ans = []
for i in range(n - m + 1):
    for j in range(n - m + 1):
        area = [[] for _ in range(m)]
        for k in range(m):
            for l in range(m):
                area[k].append(grid[i + k][j + l])
        if len(ans) == 0:
            ans.append(area)

        for g in ans:
            cnt = 0
            for k in range(m):
                for l in range(m):
                    if g[k][l] == area[k][l]:
                        cnt += 1
            if cnt == m * m:
                break
        else:
            ans.append(area)
print(len(ans))