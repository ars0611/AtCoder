import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
x = list(map(int, input().split()))
p = list(map(int, input().split()))

s = [0] * (n + 1)
for i in range(n):
    s[i + 1] = s[i] + p[i]


q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    idx_l = bisect.bisect_left(x, l)
    idx_r = bisect.bisect_right(x, r)
    print(s[idx_r] - s[idx_l])