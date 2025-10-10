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
M, D = map(int, input().split())
y, m, d = map(int, input().split())
yy = y
mm = m
dd = d
if m == M and d == D:
    yy += 1
    mm = 1
    dd = 1
elif d == D:
    mm += 1
    dd = 1
else:
    dd += 1
print(yy, mm, dd)