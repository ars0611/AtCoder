import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n = int(input())
cnt = 0
for i in range(n):
    s = input()
    if s == "sweet":
        cnt += 1
    else:
        cnt = 0
    if cnt == 2 and i != n-1:
        print("No")
        exit()
print("Yes")