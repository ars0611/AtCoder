import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, d = map(int, input().split())

value = [[] for _ in range(d)]
for i in range(n):
    x_i, y_i = map(int, input().split())
    value[x_i-1].append(-y_i)

ans = 0
heap = []
heapq.heapify(heap)
for i in range(d):
    if value[i]:
        for v in value[i]:
            heapq.heappush(heap, v)
    if heap:
        ans -= heapq.heappop(heap)

print(ans)