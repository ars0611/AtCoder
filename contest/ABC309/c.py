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
n, k = map(int, input().split())
d = defaultdict(int)
cur = 0
for _ in range(n):
    ai, bi = map(int, input().split())
    d[ai + 1] -= bi 
    cur += bi
if cur <= k:
    print(1)
else:
    for key in sorted(d.keys()):
        cur += d[key]
        if cur <= k:
            print(key)
            break