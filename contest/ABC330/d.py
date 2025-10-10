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
rows = [[] for _ in range(n)]
cols = [[] for _ in range(n)]
for i in range(n):
    s = input().strip()
    for j in range(n):
        if s[j] == "o":
            rows[i].append(j)
            cols[j].append(i)

cnt = 0
for row in rows:
    for num in row:
        cnt += (len(row) - 1) * (len(cols[num]) - 1)
print(cnt)