import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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

b = []
for i in range(n):
    record = 0
    for j in range(7):
        record += a[i * 7 + j]
    b.append(record)

print(*b)