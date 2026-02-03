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
n, w = map(int, input().split())
a = [0] + list(map(int, input().split()))
ans = set()
for i in range(n + 1):
    for j in range(n + 1):
        for k in range(n + 1):
            if i == j != 0 or i == k != 0 or j == k != 0 or i == j == k:continue
            if a[i] + a[j] + a[k] <= w :
                ans.add(a[i] + a[j] + a[k])
print(len(ans))
