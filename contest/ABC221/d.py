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
a = []
b = []
nums = set()
for i in range(n):
    ai, bi = map(int, input().split())
    a.append(ai)
    b.append(bi + ai - 1)
    nums.add(ai)
    nums.add(bi + ai - 1)
nums = sorted(list(nums))
zipped = {nums[i]:i for i in range(len(nums))}
imos = [0]*(len(nums) + 1)
for i in range(n):
    imos[zipped[a[i]]] += 1
    imos[zipped[b[i]] + 1] -= 1
    print(imos)
for i in range(1, len(nums) + 1):
    imos[i] += imos[i - 1]
ans = [0]*n
for i in range(1, len(nums)):
    ans[imos[i] - 1] += zipped[]
print(*ans)
print(imos)
print(zipped)

# 後で解く。誤読してたからやり直した方が早い

