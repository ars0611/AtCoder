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
n, q = map(int, input().split())
wht = n
seg = SortedList()
for i in range(q):
    l, r = map(int, input().split())
    idx = seg.bisect_left((l, 0))
    if idx > 0 and seg[idx - 1][1] >= l - 1:
        idx -= 1
    
    rem = 0
    nl, nr = l, r
    while idx < len(seg) and seg[idx][0] <= r + 1:
        ll, rr = seg[idx]
        nl = min(nl, ll)
        nr = max(nr, rr)
        rem += (rr - ll + 1)
        seg.pop(idx)
    seg.add((nl, nr))
    wht -= nr - nl + 1 - rem
    print(wht)
