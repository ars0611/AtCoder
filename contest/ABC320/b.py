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
s = list(input().strip())
ans = 0
for i in range(len(s), 0, -1):
    for j in range(len(s) - i + 1):
        if s[j:j + i] ==  list(reversed(s[j:j + i])):
            ans = max(ans, i)
print(ans)