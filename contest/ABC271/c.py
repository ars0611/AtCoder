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
a = deque(sorted(set((map(int, input().split())))))
cur = 0
cnt = n - len(set(a))
while a:
    if a[0] == cur + 1:
        cur += 1
        a.popleft()
    else:
        while a and cnt < 2:
            a.pop()
            cnt += 1
        if cnt >= 2:
            cur += 1
            cnt -= 2
cur += cnt // 2
print(cur)
