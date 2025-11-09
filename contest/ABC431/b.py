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
x = int(input())
n = int(input())
w = list(map(int, input().split()))
q = int(input())
wear = set()
weight = x
for _ in range(q):
    p = int(input())
    if p - 1 in wear:
        wear.discard(p - 1)
        weight -= w[p - 1]
    else:
        wear.add(p - 1)
        weight += w[p - 1]
    print(weight)