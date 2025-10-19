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
s, a, b, x = map(int, input().split())
sec = 1
ans = 0
while sec <= x:
    if 1 <= sec % (a + b) <= a:
        ans += s
    sec += 1
print(ans)