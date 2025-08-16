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
n, m = map(int, input().split())
s = list(input())
t = list(input())
swaps = [0]*n
for i in range(m):
    l,r = map(int, input().split())
    l -= 1
    r -= 1
    swaps[l] += 1
    if r + 1 < n:
        swaps[r + 1] -= 1

for i in range(1, n):
    swaps[i] += swaps[i-1]

for i in range(n):
    if swaps[i] % 2 == 1:
        s[i] = t[i]
print("".join(s))