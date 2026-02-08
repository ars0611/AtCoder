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
n, d = map(int, input().split())
a = list(map(int, input().split()))

nums = SortedList([-10 ** 9, 2 * 10 ** 9])
ans = 0
r = 0
for l in range(n):
    while r < n:
        idx = nums.bisect(a[r])
        if nums[idx] - a[r] < d or a[r] - nums[idx - 1] < d: break
        nums.add(a[r])
        r += 1
    ans += r - l
    nums.discard(a[l])
print(ans)

# 尺取りで区間を調べたい
# 今まででた数でa[r]との差がd未満になるやつがあるかを高速に調べたい
# Sortedlistを用いればできる。俺はなぜかセグ木を思い浮かべたせいで実装がむずくなって詰んだ

# ガチの解説ACだけどこの尺取りの仕方を俺は知らないかもしれない
# a[r]を追加していくわけだけど、追加できなくなったら、一緒になれないa[r]との差がd未満なa[i]を求めてl = i + 1として再スタートしたい
# それをやるためにlをfor文で実装しているのか
