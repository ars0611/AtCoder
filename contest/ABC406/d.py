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
h, w, n = map(int, input().split())
r = [SortedList() for _ in range(h)]
c = [SortedList() for _ in range(w)]
for _ in range(n):
    x, y = map(int, input().split())
    r[x - 1].add(y - 1)
    c[y - 1].add(x - 1)

q = int(input())
for _ in range(q):
    query, num = map(int, input().split())
    if query == 1:
        print(len(r[num - 1]))
        for col in r[num - 1]:
            c[col].discard(num - 1)
        r[num - 1].clear()
    else:
        print(len(c[num - 1]))
        for row in c[num - 1]:
            r[row].discard(num - 1)
        c[num - 1].clear()