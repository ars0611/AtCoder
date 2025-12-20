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
a = sorted(list(map(int, input().split())))
l = 0
intervalSumArray = []
while l < n:
    intervalSum = a[l]
    r = l + 1
    while r < n and a[r] - a[r - 1] <= 1:
        intervalSum += a[r]
        r += 1
    intervalSumArray.append(intervalSum)
    l = r
if a[0] == 0 and a[-1] == m - 1 and len(intervalSumArray) > 1:
    intervalSumArray.append(intervalSumArray[0] + intervalSumArray[-1])
print(sum(a) - max(intervalSumArray))
