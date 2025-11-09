import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
n = int(input())
movies = [tuple(map(int, input().split())) for _ in range(n)]
movies.sort(key=lambda x: x[1])
t = 0
cnt = 0
for i in range(n):
    start, end = movies[i]
    if t <= start:
        cnt += 1
        t = end
print(cnt)