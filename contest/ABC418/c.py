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
a = list(map(int, input().split()))

a.sort()
s = [0]*(n+1)
for i in range(1, n+1):
    s[i] = s[i-1] + a[i-1]

for i in range(q):
    b_i = int(input())
    
    if b_i == 1:
        print(1)
        continue
    if b_i > a[-1]:
        print(-1)
        continue

    idx = bisect.bisect_left(a, b_i)
    print(s[idx] + a[idx-1]*(n-idx) + (b_i - a[idx-1]-1) * (n-idx) + 1)