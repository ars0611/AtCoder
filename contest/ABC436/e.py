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
n = int(input())
p = list(map(lambda x:int(x) - 1, input().split()))

ans = 0
visited = [False]*n
for i in range(n):
    if visited[i]: continue
    cnt = 0
    cur = i
    while not visited[cur]:
        visited[cur] = True
        cnt += 1
        cur = p[cur]
    if cnt >= 2:
        ans += cnt * (cnt - 1) // 2
    a = []
    for i in range(n):
        if not visited[i]:
            a.append(p[i] + 1)
    print(*a)
print(ans)
