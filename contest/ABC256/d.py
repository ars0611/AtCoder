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
n = int(input())
seg = sorted(list(tuple(map(int, input().split())) for _ in range(n)))
curLeft, curRight = seg[0]
for i in range(n + 1):
    if i < n:
        li, ri = seg[i]
    if i == n or curRight < li:
        print(curLeft, curRight)
        curLeft = li
        curRight = ri
    else:
        curRight = max(curRight, ri)
