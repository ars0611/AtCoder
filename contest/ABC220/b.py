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
k = int(input())
a, b = input().split()
pa = 0
pb = 0
for d in range(len(a)):
    pa += k ** d * int(a[-1 - d])
for d in range(len(b)):
    pb += k ** d * int(b[-1 - d])
print(pa * pb)
