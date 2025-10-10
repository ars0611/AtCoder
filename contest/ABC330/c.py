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
d = int(input())
root_d = math.isqrt(d)
ans = float("inf")
for x in range(1, root_d + 1):
    y = math.isqrt(abs(d - x**2))
    diff = min(abs(d - (x**2 + y**2)), abs(d - (x**2 + (y + 1)**2)))
    ans = min(ans, diff)
print(ans)