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
s = input().strip()
t = input().strip()
cur = 0
ans = []
for i in range(len(t)):
    if t[i] == s[cur]:
        ans.append(i+1)
        cur += 1

print(*ans)