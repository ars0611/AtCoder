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
a = list(map(int,input().split()))
p = [0]*4

for i in range(4):
    p[a[i]-1] += 1

ans = 0
for i in range(4):
    if p[i] >= 2:
        ans += 1
    if p[i] == 4:
        ans += 1
print(ans)