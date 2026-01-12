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
def dfs(prev, u):
    if len(u) == n:
        res = []
        if u != sorted(u): return
        for i in range(n):
            res.append(u[i] + l[i])
        return print(*res)
    for i in range(prev, k + 1):
        dfs(i, u + [i])

n, m = map(int, input().split())
k = m - n
l = list(range(1, n + 1))
dfs(0, [])

# ToDo: DFSで配り方全探索するやつライブラリ化しよう
# なんかcombinationsというライブラリで解決する説がある
# 
