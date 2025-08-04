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
n, r = map(int, input().split())

for _ in range(n):
    d_i, a_i = map(int, input().split())
    if d_i == 1 and 1600 <= r <= 2799:
        r += a_i
    elif d_i == 2 and 1200 <= r <= 2399:
        r += a_i

print(r)