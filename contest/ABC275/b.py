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
a, b, c, d, e, f = map(int, input().split())
mod = 998244353
print((((a % mod) * (b % mod) * (c % mod)) % mod - ((d % mod) * (e % mod) * (f % mod)) % mod) % mod)
