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
n, q = map(int, input().split())
oldest = 0
cnt = [1 for _ in range(n)]
for _ in range(q):
    x, y = map(int, input().split())
    if x < oldest:
        print(0)
        continue
    ans = 0
    for i in range(x - oldest):
        ans += cnt[i + oldest]
    print(ans)

    cnt[y - 1] += ans
    oldest = x