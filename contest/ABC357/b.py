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
s = input()
u = 0
l = 0
for c in s:
    if c.isupper():
        u += 1
    else:
        l += 1

if u >= l:
    print(s.upper())
else:
    print(s.lower())