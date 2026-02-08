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
n, k = map(int, input().split())
s = [input().strip() for _ in range(n)]
cnt = [Counter(si) for si in s]
ans = 0
for bit in range(2 ** n):
    chars = defaultdict(int)
    for b in range(n):
        if bit & (1 << b):
            for ch in "abcdefghijklmnopqrstuvwxyz":
                chars[ch] += cnt[b][ch]
    kinds = 0
    for v in chars.values():
        if v == k:
            kinds += 1
    ans = max(ans, kinds)

print(ans)
