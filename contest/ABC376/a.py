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
n, c = map(int, input().split())
t = list(map(int, input().split()))

ans = 1
time = [t[0]]
for i in range(1,n):
    if t[i] - time[-1] >= c:
        ans += 1
        time.append(t[i])
print(ans)