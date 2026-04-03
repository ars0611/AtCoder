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
n, m = map(int, input().split())
takahashi = [set() for _ in range(n)]
aoki = [set() for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x:int(x) - 1, input().split())
    takahashi[a].add(b)
    takahashi[b].add(a)
for _ in range(m):
    c, d = map(lambda x:int(x) - 1, input().split())
    aoki[c].add(d)
    aoki[d].add(c)
for p in itertools.permutations(list(range(n))):
    flg = True
    for a in range(n):
        for b in takahashi[a]:
            if not p[b] in aoki[p[a]]:
                flg = False
                break
    if flg:
        print("Yes")
        break
else:
    print("No")
