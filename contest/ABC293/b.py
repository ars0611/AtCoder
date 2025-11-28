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
isCalled = [False]*n
for i in range(n):
    if not isCalled[i]:
        isCalled[a[i] - 1] = True

k = 0
x = list()
for i in range(n):
    if not isCalled[i]:
        x.append(i + 1)
        k += 1

print(k)
print(*x)