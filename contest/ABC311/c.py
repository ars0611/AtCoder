import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
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
def dfs(cur):
    if seen[cur]:
        global p
        p = cur
        return
    seen[cur] = True
    nxt = a[cur]
    dfs(nxt)
    return

n = int(input())
a = list(map(int, input().split()))
a = [ai - 1 for ai in a]

seen = [False]*n
for i in range(n):
    if not seen[i]:
        dfs(i)
        break

b = [p + 1]
cur = a[p]
while cur != p:
    b.append(cur + 1)
    cur = a[cur]

print(len(b))
print(*b)