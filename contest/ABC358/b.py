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
n, a = map(int, input().split())
t = list(map(int, input().split()))
cur = 0
for i in range(n):
    if cur  >= t[i]:
        cur += a
    else:
        cur = t[i] + a
    print(cur)