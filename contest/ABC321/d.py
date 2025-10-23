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
n, m, p = map(int, input().split())
a = list(map(int, input().split()))
b = sorted(list(map(int, input().split())))
pre_sum_b = [0]
for i in range(m):
    pre_sum_b.append(pre_sum_b[-1] + b[i])
ans = 0
for i in range(n):
    idx = bisect.bisect_right(b, p - a[i])
    ans += p * (m - idx) + pre_sum_b[idx] + (idx * a[i])

print(ans)