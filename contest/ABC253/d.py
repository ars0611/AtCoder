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
from functools import cmp_to_key
#----------------------------------------#
n, a, b = map(int, input().split())
g = a * b // math.gcd(a, b)
ans = n * (n + 1) // 2
cntA = n // a
cntB = n // b
cntG = n // (g)
ans -= a * cntA * (cntA + 1) // 2 + b * cntB * (cntB + 1) // 2 - g * cntG * (cntG + 1) // 2
print(ans)
