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
n = int(input())
sky = [[0]*2001 for _ in range(2001)]
cloud = [tuple(map(int, input().split())) for _ in range(n)]
for i in range(n):
    l, r, u, d = cloud[i]
    sky[u - 1][l - 1] += 1
    sky[u - 1][r] -= 1
    sky[d][l - 1] -= 1
    sky[d][r] += 1
for i in range(2001):
    for j in range(1, 2001):
        sky[i][j] += sky[i][j - 1]
for j in range(2001):
    for i in range(1, 2001):
        sky[i][j] += sky[i - 1][j]

s = 0
presum = [[0]*2001 for _ in range(2001)]
for i in range(2000):
    for j in range(2000):
        if sky[i][j] == 0:
            s += 1
        if sky[i][j] == 1:
            presum[i + 1][j + 1] = 1
for i in range(2001):
    for j in range(1, 2001):
        presum[i][j] += presum[i][j - 1]
for j in range(2001):
    for i in range(1, 2001):
        presum[i][j] += presum[i - 1][j]

for i in range(n):
    l, r, u, d = cloud[i]
    res = s + presum[d][r] - presum[u - 1][r] - presum[d][l - 1] + presum[u - 1][l - 1]
    print(res)
