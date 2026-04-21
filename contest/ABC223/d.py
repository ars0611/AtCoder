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
n, m = map(int, input().split())
rel = [SortedList() for _ in range(n)]
for _ in range(m):
    a, b = map(lambda x:int(x) - 1, input().split())
    rel[b].add(a)
print(rel)

# 後で解く
# 辞書順は小さいほうから貪欲。条件を満たしきった自由におけるやつの小さいほうから置きたい
