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
a, b, c, d, e, f, x = map(int, input().split())
takahashi = x // (a + c) * b * a
takahashi += a * b if x % (a + c) >= a else x % (a + c) * b
aoki = x // (d + f) * e * d
aoki += d * e if x % (d + f) >= d else x % (d + f) * e
if takahashi > aoki:
    print('Takahashi')
elif takahashi == aoki:
    print('Draw')
else:
    print('Aoki')
