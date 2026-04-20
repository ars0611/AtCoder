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
def comp(a, b, c):
    xa, ya = a
    xb, yb = b
    xc, yc = c
    return (yb - ya) * (xc - xa) == (yc - ya) * (xb - xa)
n = int(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]
ans = 0
for i in range(n - 2):
    for j in range(i + 1, n - 1):
        for k in range(j + 1, n):
            if comp(pos[i], pos[j], pos[k]): continue
            ans += 1
print(ans)
