import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter
from collections import deque
from collections import defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq
import bisect
import math
import itertools
import copy

#----------------------------------------#
n = int(input())
cur_l = 0
cur_r = 0
ans = 0
for i in range(n):
    
    a, s = input().split()
    a = int(a)
    
    if cur_l == 0 and s == "L":
        cur_l = a
        continue
    elif cur_r == 0 and s == "R":
        cur_r = a
        continue
    
    if s == "L":
        ans += abs(cur_l - a)
        cur_l = a
    else:
        ans += abs(cur_r - a)
        cur_r = a
print(ans)