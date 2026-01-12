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
s = [input().strip() for _ in range(n)]
created = defaultdict(int)
for i in range(n):
    suf = "(" + str(created[s[i]]) + ")" if created[s[i]] != 0 else ""
    print(s[i] + suf)
    created[s[i]] += 1
