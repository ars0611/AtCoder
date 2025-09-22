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
a = list(map(int, input().split()))
imos = [0]*(n)
for i in range(n):
    if i > 0:
        imos[i] += imos[i - 1]
    a[i] += imos[i]
    if a[i] > 0:
        if i + 1 < n:
            imos[i + 1] += 1
        if n - i > a[i]:
            if i + a[i] + 1 < n:
                imos[i + a[i] + 1] -= 1
            a[i] -= a[i]
        else:
            a[i] -= n - i - 1

print(*a)

# いもしながら配ればよいのでは？