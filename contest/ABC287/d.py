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
s = input().strip()
t = input().strip()
n = len(t)
pre_cmp = [False]*(n + 1)
pre_cmp[0] = True
suf_cmp = [False]*(n + 1)
suf_cmp[0] = True
for x in range(1, n + 1):
    if pre_cmp[x - 1] and (s[x - 1] == t[x - 1] or s[x - 1] == "?" or t[x - 1] == "?"):
        pre_cmp[x] = True
    if suf_cmp[x - 1] and (s[-x] == t[-x] or s[-x] == "?" or t[-x] == "?"):
        suf_cmp[x] = True
for x in range(n + 1):
    print("Yes" if pre_cmp[x] and suf_cmp[n - x] else "No")
