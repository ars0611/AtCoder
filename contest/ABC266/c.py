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
p = [tuple(map(int, input().split())) for _ in range(4)]
s = 0
for k in range(4):
    ax, ay = p[(k - 1) % 4]
    bx, by = p[k]
    cx, cy = p[(k + 1) % 4]
    r = math.degrees(math.atan2(ay - by, ax - bx) - math.atan2(cy - by, cx - bx))
    r %= 360
    if 180 < r:
        print("No")
        break
else:
    print("Yes")
