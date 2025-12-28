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
h, w, rs, cs = map(int, input().split())
n = int(input())
wall = defaultdict(SortedSet)
for i in range(n):
    r, c = map(int, input().split())
    wall[r].add(c)
    wall[h + c].add(r)
curR = rs
curC = cs
q = int(input())
for _ in range(q):
    wall[curR].add(0)
    wall[curR].add(w + 1)
    wall[h + curC].add(0)
    wall[h + curC].add(h + 1)
    d, l = input().split()
    l = int(l)
    if d == "L":
        idx = wall[curR].bisect_left(curC)
        curC = curC - l if curC - wall[curR][idx - 1] > l else wall[curR][idx - 1] + 1
    elif d == "R":
        idx = wall[curR].bisect_left(curC)
        curC = curC + l if wall[curR][idx] - curC > l else wall[curR][idx] - 1
    elif d == "U":
        idx = wall[h + curC].bisect_left(curR)
        curR = curR - l if curR - wall[h + curC][idx - 1] > l else wall[h + curC][idx - 1] + 1
    else:
        idx = wall[h + curC].bisect_left(curR)
        curR = curR + l if wall[h + curC][idx] - curR > l else wall[h + curC][idx] - 1
    print(curR, curC)
