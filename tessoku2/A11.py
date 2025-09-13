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
n, x = map(int, input().split())
a = list(map(int, input().split()))

left = 0
right = n - 1
while left < right:
    mid = (left + right) // 2
    if a[left] <= x <= a[mid]:
        right = mid
    else:
        left = mid + 1
print(right + 1)

# なんどなくbisectを縛ってみた