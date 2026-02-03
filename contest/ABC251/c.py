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
n = int(input())
s = set()
mvp = 0
mvpScore = 0
for i in range(n):
    si, ti = input().split()
    ti = int(ti)
    if si not in s and ti > mvpScore:
        mvp = i + 1
        mvpScore = ti
    s.add(si)
print(mvp)

