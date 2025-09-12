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
a = [list(input().strip()) for _ in range(n)]
b = [list(input().strip()) for _ in range(n)]
for i in range(n):
    for j in range(n):
        if a[i][j] != b[i][j]:
            print(i + 1, j + 1, sep = " ")