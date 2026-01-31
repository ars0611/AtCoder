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
n, k = map(int, input().split())
a = list(map(int, input().split()))
swapped = a[:]
seen = [False]*n
for i in range(n):
    if seen[i]: continue
    l = []
    j = i
    while j < n:
        l.append(swapped[j])
        seen[j] = True
        j += k
    l.sort()
    for j in range(len(l)):
        swapped[i + k * j] = l[j]
a.sort()
print("Yes" if all(a[i] == swapped[i] for i in range(n)) else "No")
