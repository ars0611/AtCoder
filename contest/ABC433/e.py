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
t = int(input())
for _ in range(t):
    n, m = map(int, input().split())
    x = list(map(int, input().split()))
    y = list(map(int, input().split()))
    sortedX = sorted(x)
    sortedY = sorted(y)
    if sortedX[0] < m or sortedY[0] < n:
        print("No")
    else:
        ans = [[0]*m for _ in range(n)]
        for i in range(n):
            for j in range(m):
                