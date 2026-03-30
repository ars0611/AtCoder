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
a, n = map(int, input().split())
seen = [-1]*(10 ** 6)
q = deque([(1, -1)])
while q:
    num, cnt = q.popleft()
    if 0 < seen[num] <= cnt + 1: continue
    seen[num] = cnt + 1
    if num * a < 10 ** 6:
        q.append((num * a, cnt + 1))
    if num % 10 and int(str(num % 10) + str(num // 10)) < 10 ** 6:
        q.append((int(str(num % 10) + str(num // 10)), cnt + 1))
print(seen[n])
