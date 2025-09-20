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
n, m, k = map(int, input().split())
p = [0] * n
for _ in range(k):
    a, b = map(int, input().split())
    a -= 1
    p[a] += 1
    if p[a] == m:
        print(a + 1)