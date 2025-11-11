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
#----------------------------------------#
# B39 をheapqで実装してみよう！のコーナー
n, d = map(int, input().split())
jobs = sorted(list(tuple(map(int, input().split()))) for _ in range(n))
today = 1

ans = 0
i = 0
heap = []
heapq.heapify(heap)
while i < n:
    while i < n and jobs[i][0] <= today:
        heapq.heappush(heap, -jobs[i][1])
        i += 1
    if heap:
        ans -= heapq.heappop(heap)
    today += 1

while heap and today <= d:
    ans -= heapq.heappop(heap)
    today += 1
print(ans)