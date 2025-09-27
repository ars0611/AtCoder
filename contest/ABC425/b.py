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
s = set()
for i in range(n):
    if a[i] == -1:
        continue
    if a[i] in s:
        print("No")
        break
    s.add(a[i])
else:
    p = a[:]
    ss = set(range(1, n+1)) - s
    for i in range(n):
        if p[i] == -1:
            p[i] = ss.pop()
    print("Yes")
    print(*p)