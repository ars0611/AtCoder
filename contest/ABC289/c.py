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
g = []
for _ in range(m):
    c = int(input())
    a = set(map(int, input().split()))
    g.append(a)

ans = 0
for bit in range(1 << m):
    s = set()
    for i in range(m):
        if bit & (1 << i):
            s |= g[i]
    if s == set([i + 1 for i in range(n)]):
        ans += 1
print(ans)
