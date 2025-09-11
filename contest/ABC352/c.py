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
a = []
b = []
s = 0
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi)
    s += ai

ans = 0
for i in range(n):
    ans = max(s-a[i]+b[i], ans)
print(ans)