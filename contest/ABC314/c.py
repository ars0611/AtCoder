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
s = input().strip()
c = list(map(int, input().split()))

idx = defaultdict(list)
for i in range(n):
    idx[c[i] - 1].append(i)

ans = [""]*n
for i in range(m):
    for j in range(len(idx[i])):
        ans[idx[i][j]] = s[idx[i][(j - 1) % len(idx[i])]]
print("".join(ans))