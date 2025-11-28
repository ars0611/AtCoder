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
a = list(map(int, input().split()))

d = [defaultdict(int) for _ in range(11)]
for i in range(n):
    l = len(str(a[i])) - 1
    d[l][a[i] % m] += 1

ans = 0
for i in range(n):
    for j in range(11):
        ans += d[j][(m - (a[i]*10**(j + 1)) % m) % m]

print(ans)