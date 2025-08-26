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
a, b, c, d, e, f = map(int, input().split())
g, h, i, j, k, l = map(int, input().split())

if l <= c or f <= i or j <= a or d <= g or k <= b or e <= h:
    print("No")
else:
    print("Yes") 