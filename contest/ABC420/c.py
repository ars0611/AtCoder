import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, q = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

use = []
s = 0
for i in range(n):
    s += min(a[i], b[i])
    use.append(min(a[i], b[i]))

for _ in range(q):
    c, x, y = input().split()
    x, y = int(x), int(y)
    if c == "A":
        a[x - 1] = y
    else:
        b[x - 1] = y
    s -= use[x - 1]
    use[x - 1] = min(a[x - 1], b[x - 1])
    s += use[x - 1]

    print(s)