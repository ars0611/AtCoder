import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations

#----------------------------------------#
d, n = map(int, input().split())
hours = [24]*d
for _ in range(n):
    l, r, h = map(int, input().split())
    for i in range(l - 1, r):
        hours[i] = min(hours[i], h)

print(sum(hours))