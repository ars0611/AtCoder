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
def f(a, b):
    return a * a * a + a * a * b + a * b * b + b * b * b
n = int(input())
x = 10 ** 18
for a in range(10 ** 6 + 1):
    l = -1
    r = 10 ** 6
    while r - l > 1:
        m = (l + r) // 2
        if f(a, m) >= n:
            r = m
        else:
            l = m
    x = min(x, f(a, r))
print(x)

# a = 10 ** 6, b = 0 のとき、x = 10 ** 18（>= n）が言えることから、a, b <= 10 ** 6が言える。
# いつもの二分探索だとなんかうまくいかなかって萎えたのでこれからめぐる式二分探索する
# r - l > 1でループ回して、return rする形
