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
h, w = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
flg = True
for i in range(h - 1):
    for j in range(w - 1):
        for ii in range(i + 1, h):
            for jj in range(j + 1, w):
                if a[i][j] + a[ii][jj] > a[ii][j] + a[i][jj]:
                    flg = False
print("Yes" if flg else "No")
