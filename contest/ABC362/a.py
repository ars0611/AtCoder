import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
r, g, b = map(int, input().split())
c = input()
if c == "Red":
    print(min(g, b))
elif c == "Green":
    print(min(r, b))
elif c == "Blue":
    print(min(r, g))