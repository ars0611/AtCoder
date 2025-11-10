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
a = list(map(int, input().split()))

c = Counter()
for ai in a:
    c[ai % 100] += 1

cnt = 0
for num in range(0, 51):
    if c[num] == 0: continue
    if num == 0 or num == 50:
        cnt += c[num] * (c[num] - 1) // 2
    else:
        cnt += c[num] * c[100 - num]

print(cnt)