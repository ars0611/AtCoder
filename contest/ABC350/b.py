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
n, q = map(int, input().split())
t = list(map(int, input().split()))
b = [True] * n
for i in range(q):
    b[t[i] - 1] = not b[t[i] - 1]
print(b.count(True))