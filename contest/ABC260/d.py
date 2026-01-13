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
n, k = map(int, input().split())
p = list(map(int, input().split()))
bundles = SortedList()
tops = SortedList()
ans = ["-1"]*n
for i in range(n):
    idx = bundles.bisect_left([p[i]])
    if idx == len(bundles):
        bundles.add(SortedList([p[i]]))
    else:
        bundles[idx].add(p[i])
    if len(bundles[idx]) == k:
        for num in bundles[idx]:
            ans[num - 1] = f"{i + 1}"
        bundles.discard(bundles[idx])
print("\n".join(ans))
