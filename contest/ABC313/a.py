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
n = int(input())
p = list(map(int, input().split()))
if n == 1:
    print(0)
else:
    print(max(p[1:]) - p[0] + 1 if max(p[1:]) >= p[0] else 0)