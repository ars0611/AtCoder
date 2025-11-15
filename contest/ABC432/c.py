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
from math import gcd
#----------------------------------------#
n, x, y = map(int, input().split())
a = sorted(list(map(int, input().split())))
d = y - x
mod = a[0] * x % d
if a[0] * y < a[n - 1] * x or not all(a[i] * x % d == mod for i in range(n)):
    print(-1)
else:
    ans = a[0]
    aim = a[0] * y
    for i in range(1, n):
        ans += (aim - (a[i] * x)) // d
    print(ans)