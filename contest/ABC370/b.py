import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
ele = [[0]*n for _ in range(n)]
for i in range(n):
    a = list(map(int, input().split()))
    for j, a in enumerate(a):
        ele[i][j] = a-1
        ele[j][i] = a-1

cur_ele = 0
for i in range(n):
    cur_ele = ele[cur_ele][i]

print(cur_ele+1)