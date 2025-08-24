import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, k = map(int, input().split())
s = input()
cnt = 0
for li in distinct_permutations(s):
    ok = True
    for i in range(n - k + 1):
        j = 0
        pal = True
        while j < k // 2 and pal:
            if li[i + j] != li[i + k - 1 - j]:
                pal = False
            j += 1
        if pal:
            ok = False
            break
    if ok:
        cnt += 1
print(cnt)