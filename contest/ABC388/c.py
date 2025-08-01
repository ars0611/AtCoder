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
a = list(map(int,input().split()))

ans = 0
for i in range(n):
    upper = a[i] / 2
    idx = bisect.bisect_right(a,upper)
    ans += idx
print(ans)