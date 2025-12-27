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
n, m = map(int, input().split())
s = input().strip()
t = input().strip()
ans = 10 * 100 + 1
for i in range(n - m + 1):
    ss = s[i:i + m]
    cnt = 0
    for j in range(m):
        cnt += int(ss[j]) - int(t[j]) if int(ss[j]) - int(t[j]) >= 0 else 10 - int(t[j]) + int(ss[j])
    ans = min(ans, cnt)
print(ans)
