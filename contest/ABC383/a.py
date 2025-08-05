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
n = int(input())
t, v = [], []
for i in range(n):
    t_i,v_i = map(int, input().split())
    t.append(t_i)
    v.append(v_i)

sum = v[0]
for i in range(1, n):
    sum = max(0, sum - (t[i]-t[i-1]))
    sum += v[i]
print(sum)
