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
n, x = map(int, input().split())
a = list(input())
queue = deque()
queue.append(x-1)
a[x-1] = "@"
while queue:
    pos = queue.popleft()
    if pos-1 >= 0 and a[pos-1] == ".":
        a[pos-1] = "@"
        queue.append(pos-1)
    if pos+1 <= n-1 and a[pos+1] == ".":
        a[pos+1] = "@"
        queue.append(pos+1)
print("".join(a))