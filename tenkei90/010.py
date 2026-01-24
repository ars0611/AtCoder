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
from functools import lru_cache
#----------------------------------------#
n = int(input())
classes = [[0] for _ in range(2)]
for _ in range(n):
    c, p = map(int, input().split())
    classes[c - 1].append(classes[c - 1][-1] + p)
    classes[c % 2].append(classes[c % 2][-1])
q = int(input())
for _ in range(q):
    l, r = map(int, input().split())
    print(classes[0][r] - classes[0][l - 1], classes[1][r] - classes[1][l - 1])
