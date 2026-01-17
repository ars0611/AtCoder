import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
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
from functools import lru_cache
#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
p = 0
mass = [False] * 4
for i in range(n):
    mass[0] = True
    nmass = [False] * 4
    for j in range(4):
        if not mass[j]: continue
        if j + a[i] > 3:
            p += 1
        else:
            nmass[j + a[i]] = True
    mass = nmass[:]
print(p)
