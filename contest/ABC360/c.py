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
w = list(map(int, input().split()))
d = defaultdict(list)
c = Counter(a)
for i in range(n):
    d[a[i]].append(w[i])
for v in d.values():
    v.sort(reverse=True)

ans = 0
for k, v in c.items():
    while v > 1:
        ans += d[k].pop()
        v -= 1

print(ans)