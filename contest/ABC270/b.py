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
x, y, z = map(int, input().split())
if 0 < y < z and 0 < y < x or z < y < 0 and x < y < 0:
    print(-1)
else:
    if 0 < y < x and z < y or x < y < 0 and y < z:
        print(abs(z) + abs(z - x))
    else:
        print(abs(x))
