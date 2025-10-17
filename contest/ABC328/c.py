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
n, q = map(int ,input().split())
s = input().strip()

prefix_sum = [0]
for i in range(1, n):
    if s[i - 1] == s[i]:
        prefix_sum.append(prefix_sum[-1] + 1)
    else:
        prefix_sum.append(prefix_sum[-1])

for _ in range(q):
    l, r = map(int, input().split())
    print(prefix_sum[r - 1] - prefix_sum[l - 1])