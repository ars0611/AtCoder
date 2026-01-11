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
h1, w1 = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h1)]
h2, w2 = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(h2)]

flg = False
for delR in itertools.combinations(list(range(h1)), h1 - h2):
    for delC in itertools.combinations(list(range(w1)), w1 - w2):
        delR = set(delR)
        delC = set(delC)
        nR = sorted(list(set(range(h1)) - delR))
        nC = sorted(list(set(range(w1)) - delC))
        dr = {nR[i]:i for i in range(h2)}
        dc = {nC[i]:i for i in range(w2)}
        grid = [[None]*w2 for _ in range(h2)]
        for r in range(h1):
            if r in delR: continue
            for c in range(w1):
                if c in delC: continue
                grid[dr[r]][dc[c]] = a[r][c]
        flg = True if all(all(grid[i][j] == b[i][j] for j in range(w2)) for i in range(h2)) else flg
print("Yes" if flg else "No")
