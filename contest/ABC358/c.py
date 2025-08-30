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
n, m = map(int, input().split())
s = [input().strip() for _ in range(n)]
t = [[] for _ in range(n)]
for i in range(n):
    for j in range(m):
        if s[i][j] == "o":
            t[i].append(j)

ans = float('inf')
for i in range(1 << len(t)):
    ok = set()
    for j in range(len(t)):
        if i >> j & 1:
            for k in t[j]:
                ok.add(k)
    if len(ok) == m:
        ans = min(ans, bin(i).count("1"))
print(ans)

# bit全探索