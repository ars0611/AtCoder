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
divCnt = [0]*n
for i in range(1, n):
    rootN = math.isqrt(i)
    d = 1
    s = set()
    while d < rootN + 1:
        if i % d == 0:
            s.add(d)
            s.add(i // d)
        d += 1
    divCnt[i] = len(s)

ans = 0
for i in range(1, n):
    ans += divCnt[i] * divCnt[n - i]
print(ans)
