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
pos = defaultdict(list)
for i in range(n):
    pos[a[i]].append(i)
length = defaultdict(int)
for k, v in pos.items():
    length[k] = len(v)
seen = set()
ans = 0
for i in range(n):
    if i in seen: continue
    curPos = i
    curVal = a[i]
    cnt = 1
    while True:
        seen.add(curPos)
        nxt = bisect.bisect_left(pos[curVal + 1], curPos)
        if nxt == length[curVal + 1]:
            ans = max(ans, cnt)
            break
        curPos = pos[curVal + 1][nxt]
        curVal = curVal + 1
        cnt += 1
print(ans)
