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
r, c = map(int, input().split())
di = [-1, 0, 1, 0]
dj = [0, 1, 0, -1]
cnt = 0
for k in range(4):
    ni = r + di[k]
    nj = c + dj[k]
    if 1 <= ni <= h and 1 <= nj <= w:
        cnt += 1
print(cnt)
