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
a = sorted(list(map(int, input().split())))
b = sorted(list(map(int, input().split())))

left = 0
right = 10**9 + 1
while left < right:
    mid = (left + right) // 2
    sell = bisect.bisect_right(a, mid)
    buy = m - bisect.bisect_left(b, mid)
    if sell >= buy:
        right = mid
    else:
        left = mid + 1

print(left)