import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, t, p = map(int, input().split())
l = list(map(int, input().split()))
l.sort(reverse=True)
if l[p-1] >= t:
    print(0)
else:
    print(t - l[p-1])