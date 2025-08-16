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
r_max = 0
c_max = 0
r_min = 10**9
c_min = 10**9
for i in range(n):
    r_i,c_i = map(int, input().split())
    r_max = max(r_max, r_i)
    c_max = max(c_max, c_i)
    r_min = min(r_min, r_i)
    c_min = min(c_min, c_i)

ans = max(r_max - r_min, c_max - c_min)
if ans % 2 == 0:
    print(ans // 2)
else:
    print(ans // 2 + 1)