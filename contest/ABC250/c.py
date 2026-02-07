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
a = [i + 1 for i in range(n)]
x = [int(input()) for _ in range(q)]
pos = {i + 1:i for i in range(n)}
for xq in x:
    if pos[xq] == n - 1:
        a[n - 2], a[n - 1] = a[n - 1], a[n - 2]
        pos[a[n - 2]] = n - 2
        pos[a[n - 1]] = n - 1
    else:
        idx = pos[xq]
        a[idx], a[idx + 1] = a[idx + 1], a[idx]
        pos[a[idx]] = idx
        pos[a[idx + 1]] = idx + 1
print(*a)
