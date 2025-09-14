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
a = list(map(int, input().split()))

s = [0]
for i in range(n):
    s.append(s[-1] + a[i])

l = 1
r = 1
ans = 0
while r < n + 1:

    if s[r] - s[l - 1] > k:
        l += 1
    
    else:
        ans += (r - l + 1)
        r += 1
print(ans)