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
a = list(map(int, input().split()))
x = [list(map(int,input().split())) for _ in range(n)]
ans = [0] * m
for i in range(n):
    for j in range(m):
        ans[j] += x[i][j]

for i in range(m):
    if ans[i] < a[i]:
        print("No")
        exit()

print("Yes")