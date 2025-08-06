import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
import copy

#----------------------------------------#
n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

k = max(b)
ans = [-1]*(k+1) #ans[i] := おいしさiを食べる人
for i in range(n):
    if a[i] <= k:
        ans[a[i]:k+1] = [i+1]*(k+1-a[i])
        k = a[i]-1

for i in range(m):
    print(ans[b[i]])