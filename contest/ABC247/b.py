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
name = [tuple(input().split()) for _ in range(n)]
for i in range(n):
    si, ti = name[i]
    fFlg = True
    lFlg = True
    for j in range(n):
        if i == j: continue
        sj, tj = name[j]
        if si == sj or si == tj:
            fFlg = False
        if ti == sj or ti == tj:
            lFlg = False
    if not fFlg and not lFlg:
        print("No")
        break
else:
    print("Yes")
