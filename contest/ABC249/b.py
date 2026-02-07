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
flgU = False
flgL = False
flgCh = True
chSet = set()
for ch in s:
    if ch in chSet:
        flgCh = False
    chSet.add(ch)
    if ch.isupper():
        flgU = True
    if ch.islower():
        flgL = True
print("Yes" if flgU and flgL and flgCh else "No")
