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
s = input()
c1 = 0
for ch in s:
    if ch == "1":
        c1 += 1
now = 0
ans = 0
for ch in s:
    if ch == "0":
        ans += min(now, c1 - now)
    else:
        now += 1
print(ans)
# 1をかたまりで移動させる感覚
# nowは1が登場した回数を表す
