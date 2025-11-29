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
#----------------------------------------#
t = int(input())
for _ in range(t):
    n, h = map(int, input().split())
    cursec = 0
    curmax = h
    curmin = h
    cmp = True
    for __ in range(n):
        t, l, u = map(int, input().split())
        curmax += t - cursec
        curmin -= t - cursec
        if curmax < l or curmin > u:
            cmp = False
        else:
            cursec = t
            if l <= curmax <= u:
                curmin = max(curmin, l)
            elif l <= curmin <= u:
                curmax = min(curmax, u)
            else:
                curmin = l
                curmax = u
    print("Yes" if cmp else "No")
