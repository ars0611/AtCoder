import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools

#----------------------------------------#
n, d = map(int, input().split())
t = []
l = []
for _ in range(n):
    ti, li = map(int, input().split())
    t.append(ti)
    l.append(li)

for i in range(1,d+1):
    ans = 0
    for j in range(n):
        ans = max(ans, (l[j] + i) * t[j])

    print(ans)