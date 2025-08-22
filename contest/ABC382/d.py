import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
from itertools import combinations
import copy

#----------------------------------------#
n, m = map(int, input().split())
ans = []
# 直積
def solve(v):
    size = len(v)
    if size == n:
        ans.append(v.copy())
        return
    if size == 0:
        start = 1
    else:
        start = v[-1] + 10
    limit  = m - 10*(n - size - 1)
    for i in range(start, limit + 1):
        v.append(i)
        solve(v)
        v.pop()
solve([])
print(len(ans))
for ans_i in ans:
    print(*ans_i)