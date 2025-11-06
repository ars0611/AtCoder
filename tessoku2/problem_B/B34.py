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

s = 0
for i in range(n):
    if a[i] % 5 == 4:
        s ^= 2
    elif a[i] % 5 == 3 or a[i] % 5 == 2:
        s ^= 1
    else:
        s ^= 0

print("First" if s != 0 else "Second")
# なんか実験したら grundy = [0, 0, 1, 1, 2, 0, 0, 1, 1, 2, 0,,,,,,,] な気がした。