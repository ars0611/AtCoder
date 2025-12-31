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
ans = []
for bit in range(1 << n):
    brk = []
    s = [0]
    for i in range(n):
        if bit & (1 << i):
            brk.append("(")
            s.append(s[-1] + 1)
        else:
            brk.append(")")
            s.append(s[-1] - 1)
    if min(s) >= 0 and s[-1] == 0:
        ans.append("".join(brk))
ans.sort()
for brk in ans:
    print(brk)
