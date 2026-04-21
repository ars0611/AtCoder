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
n = len(s)
shifted = set()
for i in range(n):
    shifted.add(''.join(s[i:]) + ''.join(s[:i]))
for i in range(n):
    shifted.add(''.join(s[n - i - 1:]) + ''.join(s[:n - i - 1]))
shifted = list(shifted)
shifted.sort()
print(shifted[0], shifted[-1])
