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
n, m = map(int, input().split())
revGraph = [[] for _ in range(n)]
ok = [False]*n
for _ in range(m):
    x, y = map(lambda x:int(x) - 1, input().split())
    revGraph[y].append(x)

q = int(input())
for _ in range(q):
    t, v = map(int, input().split())
    if t == 1:
        q = deque([v - 1])
        while q:
            cur = q.popleft()
            if ok[cur]: continue
            ok[cur] = True
            for nxt in revGraph[cur]:
                if not ok[nxt]:
                    q.append(nxt)
    else:
        print("Yes" if ok[v - 1] else "No")
