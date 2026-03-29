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
n = int(input())
a = [list(map(int, input().split())) for _ in range(2 * n - 1)]
dp = [-1] * (2 ** (2 * n))
print(dp[-1])
# a[k][kk - k - 1]
# n組作った時、使った人の情報を持つ添え字の要素に各xorを積む?
