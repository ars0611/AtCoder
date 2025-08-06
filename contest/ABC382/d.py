import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
import math
from collections import deque
import bisect
from collections import defaultdict
import itertools
from itertools import combinations
import copy

#----------------------------------------#
n, m = map(int, input().split())

ans = []
#
for c in combinations(list(range(1,m-9*(n-1)+1)), n):
    l = list(c)
    for i in range(1,n):
        l[i] += 9*i
    ans.append(l)

print(len(ans))
for i in ans:
    print(*i)