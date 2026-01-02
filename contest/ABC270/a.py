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
a, b = map(int, input().split())
ans = 0
ans += 1 if a % 2 == 1 or b % 2 == 1 else 0
ans += 2 if a >= 2 and a != 4 and a != 5 or b >= 2 and b != 4 and b != 5 else 0
ans += 4 if a >= 4 or b >= 4 else 0
print(ans)
