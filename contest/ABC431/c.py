import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
n, m, k = map(int, input().split())
h = sorted(list(map(int, input().split())))
b = SortedList(map(int, input().split()))

lh = len(h)
cnt = 0
for i in range(lh):
    idx = b.bisect_left(h[i])
    if idx < len(b):
        b.discard(b[idx])
        cnt += 1
    else:
        break
print("Yes" if cnt >= k else "No")