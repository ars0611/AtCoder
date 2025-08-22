import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n = int(input())
a = list(map(int, input().split()))
ans = [(a_i, i+1) for i, a_i in enumerate(a)]
ans.sort(reverse=True)
print(ans[1][1])