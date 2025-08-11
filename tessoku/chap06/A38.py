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
d, n = map(int, input().split())

t = [24] * d
for i in range(n):
    l, r, h = map(int, input().split())
    for i in range(l-1,r):
        t[i] = min(t[i], h)

print(sum(t))