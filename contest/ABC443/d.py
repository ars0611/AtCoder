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
t = int(input())
for _ in range(t):
    n = int(input())
    r = list(map(int, input().split()))
    l = r[:]
    for i in range(1, n):
        l[i] = min(r[i], l[i - 1] + 1)
    ll = r[:]
    for i in range(1, n):
        ll[n - i - 1] = min(r[n - i - 1], ll[n - i] + 1)
    ans = 0
    for i in range(n):
        ans += r[i] - min(l[i], ll[i])
    print(ans)
