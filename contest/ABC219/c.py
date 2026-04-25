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
def keyFunc(a, b):
    n = min(len(a), len(b))
    if a == b:
        return 0
    for i in range(n):
        if a[i] != b[i]:
            if p[a[i]] < p[b[i]]: return -1
            else: return 1
    if len(a) < len(b): return -1
    return 1
x = input().strip()
p = {x[i]: i for i in range(26)}
n = int(input())
s = [input().strip() for _ in range(n)]
ans = sorted(s, key=cmp_to_key(keyFunc))
print('\n'.join(ans))
