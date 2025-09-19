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
n, m = map(int, input().split())
painted = []
for _ in range(m):
    x, y, c = input().split()
    x = int(x)
    y = int(y)
    painted.append((x,y,c))
painted.sort()
min_y = float('inf')
for x, y, c in painted:
    if c == "W":
        min_y = min(min_y, y)
    else:
        if y >= min_y:
            print("No")
            break
else:
    print("Yes")