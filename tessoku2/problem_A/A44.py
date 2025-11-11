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
n, q = map(int, input().split())
a = list(i + 1 for i in range(n))
is_reversed = False
for _ in range(q):
    query = list(map(int, input().split()))

    if query[0] == 1:
        x, y = query[1] - 1, query[2]
        if is_reversed:
            a[- x - 1] = y
        else:
            a[x] = y

    elif query[0] == 2:
        is_reversed = not is_reversed

    else:
        x = query[1] - 1
        if is_reversed:
            print(a[- x - 1])
        else:
            print(a[x])