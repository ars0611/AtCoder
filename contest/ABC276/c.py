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
p = list(map(int, input().split()))

ans = []
for i in range(n):
    c = 0
    for j in range(i, n):
        if p[i] > p[j] > c:
            c = p[j]
    if not c: continue
    ans = p[:i] + [c]
    s = set(ans)
    for j in range(n, 0, -1):
        if j in s: continue
        ans += [j]
print(*ans)
