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
n, m, b = map(int, input().split())
a = list(map(int, input().split()))
c = list(map(int, input().split()))

s = sum(c)
ans = 0
for i in range(n):
    ans += a[i] * m + s + b*m
print(ans)