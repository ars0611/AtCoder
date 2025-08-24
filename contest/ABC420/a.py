import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
x, y = map(int, input().split())
if (x + y) % 12 != 0:
    print((x + y) % 12)
else:
    print(12)