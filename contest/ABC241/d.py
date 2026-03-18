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
a = SortedList()
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
l = 0
for i in range(q):
    if query[i][0] == 1:
        x = query[i][1]
        a.add(x)
        l += 1
    elif query[i][0] == 2:
        x, k = query[i][1], query[i][2]
        idx = a.bisect_right(x)
        print(a[idx - k] if idx - k >= 0 else -1)
    else:
        x, k = query[i][1], query[i][2]
        idx = a.bisect_left(x)
        print(a[idx + k - 1] if l > idx + k - 1 else -1)
