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
n, m, t = map(int, input().split())
a = list(map(int, input().split()))
b = defaultdict(int)
for _ in range(m):
    x, y = map(int, input().split())
    b[x - 1] = y

curRoom = 0
curTime = t
for i in range(n - 1):
    if curTime - a[i] > 0:
        curRoom += 1
        curTime -= a[i]
        curTime += b[i + 1]
    else: break
print("Yes" if curRoom == n - 1 else "No")
