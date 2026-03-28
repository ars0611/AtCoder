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
s = input().strip()
l = len(s)
pref = l - 1
suf = 0
for i in range(l - 1, -1, -1):
    if s[i] != 'a':
        pref = i
        break
for i in range(l):
    if s[i] != 'a':
        suf = i
        break
t = s[suf:pref + 1]
ll = len(t)
for i in range(ll // 2):
    if t[i] != t[- i - 1]:
        print("No")
        break
else:
    print("Yes" if l - pref >= suf + 1 else "No")
