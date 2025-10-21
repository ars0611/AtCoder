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
win_count = [[] for _ in range(n)]
for i in range(n):
    si = input().strip()
    win = si.count("o")
    win_count[win].append(i + 1)
ans = []
for i in range(n - 1, -1, -1):
    ans += sorted(win_count[i])
print(*ans)