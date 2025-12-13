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
grid = [[-1]*n for _ in range(n)]
grid[0][(n - 1) // 2] = 1
previ = 0
prevj = (n - 1) // 2
prevk = 1
for _ in range(n**2 - 1):
    if grid[(previ - 1) % n][(prevj + 1) % n] == -1:
        previ = (previ - 1) % n
        prevj = (prevj + 1) % n
    else:
        previ = (previ + 1) % n
        prevj = prevj
    prevk += 1
    grid[previ][prevj] = prevk
for i in range(n):
    print(*grid[i])
