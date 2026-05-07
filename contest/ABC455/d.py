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
n, q = map(int, input().split())
cards = [-1]*n
for _ in range(q):
    c, p = map(lambda x:int(x) - 1, input().split())
    cards[c] = p
nxt = dict()
keys = set()
for i in range(n):
    if i == -1: continue
    nxt[cards[i]] = i
    keys.add(cards[i])
for i in range(n):
    if cards[i] != -1:
        print(0)
        continue
    else:
        cur = i
        cnt = 1
        while cur in keys:
            cnt += 1
            cur = nxt[cur]
        print(cnt)
