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
n, q = map(int, input().split())

l = 1
r = 2
ans = 0
for i in range(q):
    h, t = input().split()
    t = int(t)

    if h == "R":
        if t <= r:
            if not(t <= l <= r):
                ans += r - t
            else:
                ans += n - r + t
        else:
            if not(r <= l <= t):
                ans += t - r
            else:
                ans += r + n - t
        r = t
    else:
        if t <= l:
            if not (t <= r <= l):
                ans += l - t
            else:
                ans += n - l + t
        else:
            if not (l <= r <= t):
                ans += t - l
            else:
                ans += l + n - t
        l = t
print(ans)