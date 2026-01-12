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
n = int(input())
a = list(map(int, input().split()))
cnt = 0
ans = 0
for i in range(n):
    cnt = cnt + 1 if a[i] == i + 1 else cnt
    ans = ans - 1 if a[i] == i + 1 else ans
    ans = ans + 1 if a[a[i] - 1] == i + 1 else ans
ans += cnt * (cnt - 1)
ans //= 2
print(ans)

# 数え上げで包除つかってる。くそ読みにくいなこれ。
