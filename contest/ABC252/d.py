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
cnter = Counter(a)
v = sorted(set(a))
s = [0]
for i in range(len(v)):
    s.append(s[-1] + cnter[v[i]])
ans = 0
for i in range(len(v)):
    ans += (s[i]) * cnter[v[i]] * (s[-1] - s[i + 1])
print(ans)

# j固定で、jより小さい値の数の個数 * jの個数 * jより大きい数の個数を加算していけばよさそう
# ソートしても良いのでソートしてランレングス圧縮した際の係数の累積和を取るとj固定した際の両サイドの個数をO(1)でとれる
