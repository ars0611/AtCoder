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
r = int(input())

def ok(i, j):
    return (2 * i + 1)**2 + (2 * j + 1)**2 <= 4 * r**2
cnt = 0
m = r - 1
for i in range(1, r):
    while not ok(i, m):
        m -= 1
    cnt += m
ans = (r - 1) * 4 + 1
ans += 4 * cnt
print(ans)