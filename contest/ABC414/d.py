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
x = list(map(int, input().split()))
x.sort()

diff = [x[i] - x[i-1] for i in range(1, n)]
diff.sort()

ans = 0
for i in range(n-m):
    ans += diff[i]
print(ans)