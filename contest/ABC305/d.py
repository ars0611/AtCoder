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
n = int(input())
a = list(map(int, input().split()))

pre_sum = [0, 0]
for i in range(1, n):
    if i % 2 == 1:
        pre_sum.append(pre_sum[-1])
    else:
        pre_sum.append(pre_sum[-1] + a[i] - a[i - 1])

q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    start = bisect.bisect_left(a, l)
    end = bisect.bisect_left(a, r)
    res = pre_sum[end + 1] - pre_sum[start]
    if start % 2 == 0:
        res -= l - a[max(start - 1, 0)]
    if end % 2 == 0:
        res -= a[end] - r
    print(res)