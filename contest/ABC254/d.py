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
def getMaxSqDivisor(k):
    rootK = math.isqrt(k)
    res = 1
    for div in range(1, rootK + 1):
        if k % div == 0:
            if k // div in sq:
                res = max(res, k // div)
            if div in sq:
                res = max(res, div)
    return res
n = int(input())
sq = set()
for i in range(1, n + 1):
    sq.add(i * i)
counter = Counter()
for i in range(1, n + 1):
    counter[i // getMaxSqDivisor(i)] += 1
ans = 0
for i in range(1, n + 1):
    ans += counter[i // getMaxSqDivisor(i)]
print(ans)
# 数学すぎてわからん
# ある整数iを素因数分解して指数の偶奇で分けて考えると i = iを割り切れる最大の平方数 * 指数が奇数の素因数の積 となる
# i * jが平方数になるのは j = i / iを割り切れる最大の平方数 * 平方数となる。
