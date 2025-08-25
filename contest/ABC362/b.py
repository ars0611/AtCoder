import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
x = []
y = []
for _ in range(3):
    xi, yi = map(int, input().split())
    x.append(xi)
    y.append(yi)
ab = (x[0] - x[1])**2 + (y[0] - y[1])**2
ac = (x[0] - x[2])**2 + (y[0] - y[2])**2
bc = (x[1] - x[2])**2 + (y[1] - y[2])**2
if ab + ac == bc or ab + bc == ac or ac + bc == ab:
    print("Yes")
else:
    print("No")