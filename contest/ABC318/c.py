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
n, d, p = map(int, input().split())
f = sorted(list(map(int, input().split())))

pre_sum = [0]
for i in range(n):
    pre_sum.append(pre_sum[-1] + f[i])

ans = sum(f)
for i in range(n // d + 2):
    price = p * i + pre_sum[max(-(n + 1), -(d * i + 1))]
    ans = min(ans, price)
print(ans)