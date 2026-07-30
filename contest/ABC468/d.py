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
s = input().strip()
n = len(s)
ans = 0
# 奇数長
for i in range(n):
    cnt = 0
    for j in range(n):
        if i - j < 0 or n <= i + j: break
        if s[i - j] != s[i + j]:
            cnt += 1
        if cnt < 2:
            ans += 1
        else: break
# 偶数長
for i in range(n - 1):
    cnt = 0
    for j in range(n):
        if i - j < 0 or n <= i + 1 + j: break
        if s[i - j] != s[i + 1 + j]:
            cnt += 1
        if cnt < 2:
            ans += 1
        else: break
print(ans)
