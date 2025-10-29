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
m = int(input())
d = list(map(int, input().split()))

center = sum(d) // 2 + 1
cnt = center
for i in range(m):
    if cnt > d[i]:
        cnt -= d[i]
        continue
    print(i + 1, cnt)
    break