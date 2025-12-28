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
a = list(map(int, input().split()))
zipped = sorted(list(set(a)))
rank = {ai:i for i, ai in enumerate(zipped)}
ans = [0]*(n)
m = len(rank)
for i in range(n):
    ans[m - rank[a[i]] - 1] += 1
for num in ans:
    print(num)
