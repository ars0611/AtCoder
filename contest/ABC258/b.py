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
#----------------------------------------#
def dfs(curi, curj, d, cnt):
    if cnt == n:
        global ans
        ans = max(ans, int("".join(nums)))
        return
    nums.append(a[curi][curj])
    ni = (curi + di[d]) % n
    nj = (curj + dj[d]) % n
    dfs(ni, nj, d, cnt + 1)
    return nums.pop()

n = int(input())
a = [input().strip() for _ in range(n)]
di = [-1, -1, 0, 1, 1, 1, 0, -1]
dj = [0, 1, 1, 1, 0, -1, -1, -1]
nums = []
ans = -1
for i in range(n):
    for j in range(n):
        for d in range(8):
            dfs(i, j, d, 0)
print(ans)
