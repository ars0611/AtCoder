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
p = [[] for _ in range(9)]
cnt = 1
p[0].append(str(cnt))
while cnt * 2 <= 10**9:
    cnt *= 2
    p[len(str(cnt)) - 1].append(str(cnt))

nums = set()
def dfs(rem, l):
    if rem == 0: return
    for k in range(1, rem + 1):
        nl = l[:] + [k]
        for v in itertools.product(*(p[d - 1] for d in nl)):
            nums.add(int(''.join(vv for vv in v)))
        dfs(rem - k, nl)
dfs(9, [])
nums = sorted(list(nums))
print(nums[n - 1])

# これ引数展開で直積のとこなんとかできたのは良いね
