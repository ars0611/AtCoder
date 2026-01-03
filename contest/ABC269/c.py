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
#----------------------------------------#
n = int(input())
nb = format(n, "b")
l = len(nb)
s = []
for i in range(l):
    if nb[i] == "1":
        s.append(l - i - 1)
ans = []
for bit in range(1 << len(s)):
    res = 0
    for i in range(len(s)):
        if bit & (1 << i):
            res += 2 ** s[i]
    ans.append(res)
ans.sort()
for res in ans:
    print(res)
