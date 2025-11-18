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
# ユークリッドの互除法による最大公約数の求値
def Euclidean_GCD(a, b):
    x = max(a, b)
    y = min(a, b)
    cnt = 0
    while y > 0:
        tmp = x % y
        cnt += x // y
        x = y
        y = tmp
    return x, y, cnt
a, b = map(int, input().split())

la, lb, cnt = Euclidean_GCD(a, b)
if la != lb:
    print(cnt - 1)
else:
    print(-1)