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
x = int(input())

ans = 0
for i in range(1,10):
    for j in range(1,10):
        p = i * j
        if p != x:
            ans += p
print(ans)