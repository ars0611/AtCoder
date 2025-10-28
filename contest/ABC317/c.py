import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
n, m = map(int, input().split())
path = defaultdict(dict)
goals = defaultdict(set)
for _ in range(m):
    a, b, c = map(int, input().split())
    a -= 1; b -= 1
    path[a][b] = c
    path[b][a] = c
    goals[a].add(b)
    goals[b].add(a)

ans = 0
for l in itertools.permutations(range(n)):
    cur = l[0]
    cnt = 0
    for i in range(1, n):
        if not l[i] in goals[cur]: break
        cnt += path[cur][l[i]]
        cur = l[i]
        ans = max(ans, cnt)
print(ans)