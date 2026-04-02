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
n, k = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for ai in a:
    s.append(s[-1] + ai)
cnter = Counter(s)
seen = Counter()
ans = 0
for i in range(n):
    seen[s[i]] += 1
    ans += cnter[k + s[i]] - seen[k + s[i]]
print(ans)
