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
n = int(input())
h = list(map(int, input().split()))

ans = 1
for i in range(n):
    height = h[i]
    for gap in range(n-i-1):
        cur = 1
        k = 1
        while True:
            if i + gap*k + k >= n or h[i+gap*k+k] != height:
                ans = max(ans,cur)
                break
            else:
                k += 1
                cur += 1
print(ans)
