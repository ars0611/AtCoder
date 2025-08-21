import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
q = int(input())
b = set()
c = Counter()
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        x = query[1]
        c[x] += 1
        b.add(query[1])

    elif query[0] == 2:
        x = query[1]
        c[x] -= 1
        if c[x] == 0:
            b.discard(x)
    else:
        print(len(b))