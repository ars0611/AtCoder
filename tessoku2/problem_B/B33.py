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
n, h, w = map(int, input().split())
nim = 0
for _ in range(n):
    a, b = map(int, input().split())
    nim ^= a - 1
    nim ^= b - 1
print("First" if nim else "Second")

# 各マスの駒について、左方向に動かせる数と上方向に動かせる数をそれぞれ石の山と見ればNim和に帰着できますよねん