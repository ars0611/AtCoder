import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
#----------------------------------------#
n, m = map(int, input().split())
solved = [set() for _ in range(n)]
for i in range(n):
    s = input().strip()
    for j in range(m):
        if s[j] == "o":
            solved[i].add(j)

cnt = 0
for i in range(n - 1):
    for j in range(i + 1, n):
        if len(solved[i].union(solved[j])) == m:
            cnt += 1
print(cnt)
