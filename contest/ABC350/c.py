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

ans = []

idx = dict()
for i, ai in enumerate(a):
    idx[ai] = i + 1

for i in range(n):
    if a[i] == i + 1:
        continue
    j = idx[i + 1]
    a[i], a[j - 1] = a[j - 1], a[i]
    idx[a[j - 1]] = j
    idx[a[i]] = i + 1
    ans.append((i + 1, j))

print(len(ans))
for x, y in ans:
    print(x, y)

# ABC421Cの類題感がある。順番に見て違うならswapする。