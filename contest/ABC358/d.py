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
n, m = map(int, input().split())
a = deque(sorted(list(map(int, input().split()))))
b = sorted(list(map(int, input().split())))

i = 0
ans = 0
while a and i < m:
    if a[0] >= b[i]:
        ans += a.popleft()
        i += 1
    else:
        a.popleft()

if i == m:
    print(ans)
else:
    print(-1)