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
h, w = map(int, input().split())
grid_a = list(input().strip() for _ in range(h))
grid_b = list(input().strip() for _ in range(h))

cmp = False
for s in range(h):
    for t in range(w):
        if all(grid_a[(i + s) % h][(j + t) % w] == grid_b[i][j] for i in range(h) for j in range(w)):
            cmp =  True

print("Yes" if cmp else "No")