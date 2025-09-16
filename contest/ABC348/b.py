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
x = []
y = []
for i in range(n):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)


for i in range(n):
    max_diff = 0
    for j in range(n):
        d = math.sqrt((x[i] - x[j]) ** 2 + (y[i] - y[j]) ** 2)
        if d > max_diff:
            ans = j + 1
            max_diff = d
    print(ans)