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
s = [input().strip() for _ in range(n)]

idx = [[] for _ in range(10)]
for i in range(n):
    for j in range(10):
        idx[int(s[i][j])].append(j)
ans = 10 * n
for i in range(10):
    replaced = set()
    for num in idx[i]:
        while num in replaced:
            num += 10
        replaced.add(num)
    ans = min(ans, max(replaced))
print(ans)
