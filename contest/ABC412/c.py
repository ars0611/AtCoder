import sys
sys.setrecursionlimit(10**6)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect

#----------------------------------------#
t = int(input())
for _ in range(t):
    n = int(input())
    s = list(map(int, input().split()))
    dmn = [s[0], s[n-1]]
    cur = s[0]
    s.sort()
    ans = 2
    while 2 * cur < dmn[-1]:
        idx = bisect.bisect_right(s, 2 * cur)
        if s[idx - 1] != cur:
            cur = s[idx - 1]
            ans += 1
        else:
            break
    if 2 * cur < dmn[-1]:
        print(-1)
    else:
        print(ans)