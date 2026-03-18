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
t = int(input())
for _ in range(t):
    n, d = map(int, input().split())
    a = list(map(int, input().split()))
    b = list(map(int, input().split()))
    q = []
    idx = 0
    for i in range(n):
        egg = b[i]
        q.append(a[i])
        while q[idx] < egg:
            egg -= q[idx]
            idx += 1
        q[idx] -= egg
        if idx + d == i:
            idx += 1
    print(sum(q[idx:]))
