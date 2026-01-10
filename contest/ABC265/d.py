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
n, p, q, r = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[-1] + a[i])
flg = False
for x in range(1, n - 1):
    y = bisect.bisect_left(s, p + s[x - 1])
    if y > n or p != s[y] - s[x - 1]: continue
    z = bisect.bisect_left(s, q + s[y])
    if z > n or q != s[z] - s[y]: continue
    w = bisect.bisect_left(s, r + s[z])
    if w > n or r != s[w] - s[z]: continue
    if x - 1 < y < z < w:
        flg = True
print("Yes" if flg else "No")

# 添え字行かれまくってガチでうざいので明日問題文をちゃんと読むところからやる
