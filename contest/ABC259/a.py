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
n, m, x, t, d = map(int, input().split())
ageToLen = [0]*(n + 1)
ageToLen[n] = t
for i in range(n - 1, -1, -1):
    if x <= i < n:
        ageToLen[i] = ageToLen[i + 1]
    else:
        ageToLen[i] = ageToLen[i + 1] - d
print(ageToLen[m])
