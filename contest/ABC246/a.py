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
x = []
y = []
for _ in range(3):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
if x[0] == x[1]:
    ansX = x[2]
elif x[1] == x[2]:
    ansX = x[0]
else:
    ansX = x[1]
if y[0] == y[1]:
    ansY = y[2]
elif y[1] == y[2]:
    ansY = y[0]
else:
    ansY = y[1]
print(ansX, ansY)
