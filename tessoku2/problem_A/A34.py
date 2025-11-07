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
n, x, y = map(int, input().split())
a = list(map(int, input().split()))
m = max(a)
grundy = [0]*(m + 1)
for i in range(m + 1):
    transit = [False]*3                 # 石の取り方が2種類しかないことから、Grundy数は3種類
    if i >= x:
        transit[grundy[i - x]] = True   # i - x個の時のGrundy数を踏むので除外
    if i >= y:
        transit[grundy[i - y]] = True   # i - xと同様
    for j in range(3):
        if not transit[j]:              # 踏んでないGrundy数の最小値がiのGrundy数
            grundy[i] = j
            break
s = 0
for i in range(n):
    s ^= grundy[a[i]]

print("First" if s != 0 else "Second")
print(grundy)