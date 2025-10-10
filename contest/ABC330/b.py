import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, l, r = map(int, input().split())
a = list(map(int, input().split()))
for i in range(n):
    if a[i] <= l:
        x = l
    elif l < a[i] < r:
        x = a[i]
    else:
        x = r
    print(x, sep=" ")
# 新発見 listにして*listより一個ずつの方が速い <- 今回はこれだった