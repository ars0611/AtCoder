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
n = input().strip()
ans = 0
for bit in range(1 << len(n)):
    l = []
    r = []
    for b in range(len(n)):
        if bit & (1 << b):
            l.append(int(n[b]))
        else:
            r.append(int(n[b]))
    if len(l) == 0 or len(l) == len(n): continue
    l.sort(reverse=True)
    r.sort(reverse=True)
    ll = int(''.join([str(l[i]) for i in range(len(l))]))
    rr = int(''.join([str(r[i]) for i in range(len(r))]))
    ans = max(ans, ll * rr)
print(ans)
