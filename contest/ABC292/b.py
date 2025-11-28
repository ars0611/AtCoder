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
n, q = map(int, input().split())
p = [0]*n
for _ in range(q):
    c, x = map(int, input().split())
    if c == 1:
        p[x - 1] += 1
    elif c == 2:
        p[x - 1] += 2
    else:
        print("Yes" if p[x - 1] >= 2 else "No")