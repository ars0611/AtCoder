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
from functools import lru_cache
#----------------------------------------#
n = int(input())
a, b, c = map(int, input().split())
cnt = 10000
for i in range(10000):
    for j in range(10000 - i):
        rem = n - i * a - j * b
        if rem < 0 or rem % c != 0: continue
        cnt = min(cnt, i + j + rem // c)
print(cnt)

# 工夫した全探索典型
