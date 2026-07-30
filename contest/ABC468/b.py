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
from functools import cmp_to_key
#----------------------------------------#
m, d = map(int, input().split())
s = input().strip()
isMonitored = [False]*m
for i in range(m):
    if s[i] == ".": continue
    for j in range(-d, d + 1, 1):
        if i + j < 0 or m - 1 < i + j: continue
        isMonitored[i + j] = True
print(isMonitored.count(False))
