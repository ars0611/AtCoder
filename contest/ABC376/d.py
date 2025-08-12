import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import bisect
import math
import itertools
import copy

#----------------------------------------#
n, m = map(int, input().split())
p = [[] for _ in range(n)]
for i in range(m):
    a, b = map(int, input().split())
    p[a-1].append(b-1)

#bfs
q = deque()
#dは0からの距離を記録
d = [m+1] * n
d[0] = 0
q.append(0)
while q:
    cur = q.popleft()
    for next in p[cur]:
        if next == 0:
            print(d[cur] + 1)
            exit()
        if d[next] == m+1:
            d[next] = d[cur] + 1
            q.append(next)
print(-1)