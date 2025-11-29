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
#----------------------------------------#
n, m = map(int, input().split())
a = list(map(int, input().split()))
re = set([(ai, ai + 1) for ai in a])
ans = []
l = 1
while l <= n:
    r = l
    while (r, r + 1) in re:
        r += 1
    ans += list(range(r, l - 1, -1))
    l = r + 1
print(*ans)
