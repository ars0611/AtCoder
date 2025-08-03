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
n,m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
for b_i in b:
    idx = bisect.bisect_left(a, b_i)
    if idx < len(a) and a[idx] == b_i:
        a.pop(idx)
for a_i in a:
    print(a_i, end=" ")