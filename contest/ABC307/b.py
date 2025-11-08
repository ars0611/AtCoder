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
s = [input().strip() for _ in range(n)]

cmp = False
for i in range(n):
    for j in range(n):
        if i == j: continue
        t = list(s[i]) + list(s[j])
        if t == t[::-1]:
            cmp = True

print("Yes" if cmp else "No")