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
a = list(map(int, input().split()))
for i in range(n - 1):
    si, ti = map(int, input().split())
    a[i + 1] += ti * (a[i] // si)

print(a[n - 1])