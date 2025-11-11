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
grid = [list(map(int, input().split())) for _ in range(n)]
row = [i for i in range(n)]
q = int(input())
for _ in range(q):
    q_type, x, y = map(int, input().split())
    x, y = x - 1, y - 1
    if q_type == 1:
        row[x], row[y] = row[y], row[x]
    else:
        print(grid[row[x]][y])