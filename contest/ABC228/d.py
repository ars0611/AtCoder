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
n = 2 ** 20
q = int(input())
query = [list(map(int, input().split())) for _ in range(q)]
a = [-1] * n
idx = SortedList([i for i in range(2 * n)])
for t, x in query:
    if t == 1:
        i = idx.bisect_left(x % n)
        a[p := idx[i] % n] = x
        idx.discard(p)
        idx.discard(p + n)
    else:
        print(a[x % n])
