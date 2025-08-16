import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, m, l = map(int, input().split())
a = list(map(int, input().split()))
s = []
for i in range(n-l+1):
    s_i = sum(a[i:i+l]) % m
    s.append(s_i)

