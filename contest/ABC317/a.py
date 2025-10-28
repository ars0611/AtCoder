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
n, h, x = map(int, input().split())
p = list(map(int, input().split()))
for i in range(n):
    if h + p[i] >= x:
        print(i + 1)
        break