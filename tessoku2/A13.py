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
n, k = map(int, input().split())
a = sorted(list(map(int, input().split())))

l = 0
r = 1
ans = 0
while r < n:
    if a[r] - a[l] > k:
        l += 1
    else:
        r += 1
        ans += (r - l - 1)
print(ans)