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
q = int(input())
s = defaultdict(int)
ss = SortedSet()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        s[x] += 1
        ss.add(x)
    elif query[0] == 2:
        x = query[1]
        c = query[2]
        if s[x] - c > 0:
            s[x] -= c
        else:
            s[x] = 0
            ss.discard(x)
    else:
        print(ss[-1] - ss[0])
