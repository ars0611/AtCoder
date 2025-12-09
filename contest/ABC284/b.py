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
    n = int(input())
    a = list(map(int, input().split()))
    cnt = 0
    for i in range(n):
        if a[i] % 2 == 1:
            cnt += 1
    print(cnt)
