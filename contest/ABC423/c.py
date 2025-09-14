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
n, r = map(int, input().split())
l = list(map(int, input().split()))
cmp_left = True
cmp_right = True
left = []
right = []
for i in range(n):
    if i < r and cmp_left and l[i] == 0:
        left = l[i:r]
        cmp_left = False
    if n - 1 - i >= r and cmp_right and l[n - 1 - i] == 0:
        right = l[r:n - i]
        cmp_right = False

ans = len(left) + len(right) + left.count(1) + right.count(1)
print(ans)