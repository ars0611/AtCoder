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
a = list(map(int, input().split()))

# n - 1回の操作がある
score = [[0]*(i + 1) for i in range(n)]
for i in range(n - 1, -1, -1):
    for j in range(i + 1):
        if i == n - 1:                  # 底辺
            score[i][j] = a[j]
        else:
            if i % 2 == 1:              # 先手後手の分岐
                score[i][j] = min(score[i + 1][j], score[i + 1][j + 1])
            else:
                score[i][j] = max(score[i + 1][j], score[i + 1][j + 1])

print(score[0][0])