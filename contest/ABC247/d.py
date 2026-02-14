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
q = int(input())
cylinder = deque()
query = [list(map(int, input().split())) for _ in range(q)]
for i in range(q):
    l = query[i]
    if l[0] == 1:
        cylinder.append([l[1], l[2]])
    else:
        res = 0
        c = l[1]
        while c:
            if cylinder[0][1] >= c:
                res += c * cylinder[0][0]
                cylinder[0][1] -= c
                c = 0
            else:
                res += cylinder[0][0] * cylinder[0][1]
                c -= cylinder[0][1]
                cylinder.popleft()
        print(res)
