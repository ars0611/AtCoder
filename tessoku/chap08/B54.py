import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
a = {}
set_a = set()
for i in range(n):
    a_i = int(input())
    if not a_i in set_a: 
        set_a.add(a_i)
        a[a_i] = 1
    else:
        a[a_i] += 1

ans = 0
for key in a.keys():
    if a[key] >= 2:
        ans += a[key] * (a[key] - 1) // 2
print(ans)