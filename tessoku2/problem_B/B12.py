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
n = int(input())
l = 0
r = 100
while l < r:
    m = (l + r) / 2
    if abs(m**3 + m - n) <= 0.001:
        print(m)
        break
    if m**3 + m < n:
        l = m
    else:
        r = m