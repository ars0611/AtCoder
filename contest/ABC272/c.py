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
a = sorted(list(map(int, input().split())))
nums = [[] for _ in range(2)]
for i in range(n):
    nums[a[i] % 2].append(a[i])
ans = -1
ans = max(nums[0][-1] + nums[0][-2], ans) if len(nums[0]) >= 2 else ans
ans = max(nums[1][-1] + nums[1][-2], ans) if len(nums[1]) >= 2 else ans
print(ans)
