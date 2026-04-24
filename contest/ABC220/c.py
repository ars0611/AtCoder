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
a = list(map(int, input().split()))
x = int(input())
s = sum(a)
ans = x // s * n
i = 0
x %= s
while x >= 0:
    x -= a[i]
    i += 1
    ans += 1
print(ans)
