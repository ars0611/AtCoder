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
n, k = map(int, input().split())
a = []
b = []
for i in range(n):
    a_i, b_i = map(int, input().split())
    a.append(a_i)
    b.append(b_i)

ans = 0
for i in range(101):
    for j in range(101):
        cnt = 0
        for l in range(n):
            if i <= a[l] <= i + k and j <= b[l] <= j+k:
                cnt += 1
        ans = max(ans, cnt)
print(ans)