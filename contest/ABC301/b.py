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
a = list(map(int, input().split()))

ans = []
for i in range(n):
    if i == n - 1:
        ans += [a[i]]
    elif a[i] < a[i + 1]:
        ans += list(range(a[i], a[i + 1]))
    else:
        ans += list(range(a[i], a[i + 1], - 1))

print(*ans)