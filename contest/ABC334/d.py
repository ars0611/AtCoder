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
r = list(map(int, input().split()))
r.sort()
s = [0]
for i in range(n):
    s.append(s[-1] + r[i])
for _ in range(q):
    x = int(input())
    idx = bisect.bisect_right(s, x)
    print(idx - 1)