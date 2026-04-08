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
n, a, b = map(int, input().split())
p, q, r, s = map(int, input().split())
bs = (a + max(1 - a, 1 - b), b + max(1 - a, 1 - b))
be = (b + min(n - a, n - b), b - min(n - a, n - b))
bbs = (a + max(1 - a, b - n), b - max(1 - 1, b - n))
bbe = (a + min(n - a, b - 1), b - min(n - a, b - 1))

ans = [['.']*(s - r + 1) for _ in range(q - p + 1)]
for i in range(s - r + 1):
    for j in range(q - p + 1):
        if bs[0] <= i + 1 <= be[0] and bs[1] <= j + 1 <= be[1]:
            if
                ans[i][j] = '#'
        if bbs[0] <= i + 1 <= bbe[0] and bbs[1] <= j + 1 <= bbe[1]:
            if 
                ans[i][j] = '#'
for i in range(s - r + 1):
    print(''.join(ans[i]))
#後で解く
