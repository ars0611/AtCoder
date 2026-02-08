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
a = list(map(int, input().split()))
cnter = Counter(a)
seen = set()
ans = 0
for ai in a:
    divs = set()
    sqrtAi = math.isqrt(ai)
    for div in range(1, sqrtAi + 1):
        if ai % div != 0: continue
        divs.add(div)
        divs.add(ai // div)
    for div in divs:
        ans += cnter[div] * cnter[ai // div]
print(ans)
