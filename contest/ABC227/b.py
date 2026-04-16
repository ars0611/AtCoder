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
n = int(input())
s = list(map(int, input().split()))
c = set()
for a in range(1, 1000):
    for b in range(1, 1000):
        c.add(4 * a * b + 3 * a + 3 * b)
ans = 0
for si in s:
    if not si in c:
        ans += 1
print(ans)
