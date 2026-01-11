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
s = list(input().strip())
t = "atcoder"
d = {ch:i for i, ch in enumerate(t)}
cnt = 0
for i in range(6):
    for j in range(i + 1, 7):
        cnt = cnt + 1 if d[s[i]] > d[s[j]] else cnt
print(cnt)
