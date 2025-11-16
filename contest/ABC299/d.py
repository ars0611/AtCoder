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
#----------------------------------------#
n = int(input())

l = 1
r = n
sl = 0
sr = 1
while l < r:
    m = (l + r) // 2
    print("?", m, flush=True)
    sm = int(input())
    if sm == sl:
        l = m + 1
        sl = sm
    else:
        r = m
        sr = sm

print("!", r - 1, flush=True)