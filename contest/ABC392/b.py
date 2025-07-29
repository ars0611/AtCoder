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
n, m = map(int,input().split())
a= list(map(int, input().split()))

x = []
set_a = set(sorted(a))
for i in range(n):
    if not i+1 in set_a:
        x.append(str(i+1))
print(len(x))
print(" ".join(x))