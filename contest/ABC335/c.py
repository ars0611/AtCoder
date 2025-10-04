import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, q = map(int, input().split())
dx, dy, m = 1, 0, 0
h = [(dx, dy)]
for _ in range(q):
    q1, q2 = input().split()
    if q1 == "1":
        c = q2
        if c == "L":
            dx += -1
        elif c == "R":
            dx += 1
        elif c == "U":
            dy += 1
        else:
            dy += -1
        m += 1
        h.append((dx, dy))
    else:
        p = int(q2)
        if p - m > 0:
            x = p - m
            y = 0
        else:
            x = h[m - p + 1][0]
            y = h[m - p + 1][1]
        print(x, y)