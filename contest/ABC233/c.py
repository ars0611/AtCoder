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
n, x = map(int, input().split())
l = []
a = []
cnter = []
for _ in range(n):
    li, *ai = list(map(int, input().split()))
    newAi = list(set(ai))
    newLi = len(newAi)
    l.append(newLi)
    a.append(newAi)
    cnter.append(Counter(ai))
cur = cnter[0]
for i in range(1, n):
    nxt = Counter()
    for j in range(l[i]):
        for p, cnt in cur.items():
            nxt[p * a[i][j]] += cnt * cnter[i][a[i][j]]
    cur = nxt
print(cur[x])
