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
n, m, d = map(int, input().split())
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

ans = -1
for i in range(n):
    idx = bisect.bisect_left(b, a[i] + d)
    if idx < m and  b[idx] == a[i] + d:
        ans = max(ans, a[i] + b[idx])
    else:
        if 0 < idx and a[i] - b[idx - 1] <= d:
            ans = max(ans, a[i] + b[idx - 1])

print(ans)