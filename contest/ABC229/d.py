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
s = input().strip()
k = int(input())
n = len(s)
ans = 0
cnt = 0
r = 0
for l in range(n):
    r = max(r, l)
    if l > 0 and s[l - 1] == '.':
        cnt = max(cnt - 1, 0)
    while r < n and cnt <= k:
        if cnt == k and s[r] == '.':
            break
        if s[r] == '.':
            cnt += 1
        r += 1
    ans = max(ans, r - l)
print(ans)

# .をk個以下しか含まないようなsubstringの長さ
# 尺取っぽくやりたい
# 後で解きますよー
