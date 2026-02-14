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
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
ans = 0
r = 0
s = SortedList()
for l in range(n):
    while r < n:
        if a[r] < y or x < a[r]: break
        s.add(a[r])
        r += 1
    ans += r - l
    s.discard(a[l])
print(ans)

# 解けてませんよー
