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
h, w, n = map(int, input().split())
choco = []
hei = defaultdict(list)
wid = defaultdict(list)
for i in range(n):
    hi, wi = map(int, input().split())
    hei[hi].append(i)
    wid[wi].append(i)
    choco.append((hi, wi))
used = set()
curh, curw = h, w
curx, cury = 0, 0
ans = [[] for _ in range(n)]
for _ in range(n):
    while hei[curh] and hei[curh][-1] in used:
        hei[curh].pop()
    if hei[curh]:
        i = hei[curh].pop()
        while hei[curh] and i in used:
            i = hei[curh].pop()
        used.add(i)
        ans[i] = [curx, cury]
        curw -= choco[i][1]
        curx += choco[i][1]
    else:
        while wid[curw] and wid[curw][-1] in used:
            wid[curw].pop()
        i = wid[curw].pop()
        while wid[curw] and i in used:
            i = wid[curw].pop()
        used.add(i)
        ans[i] = [curx, cury]
        curh -= choco[i][0]
        cury += choco[i][0]
for xi, yi in ans:
    print(yi, xi)
