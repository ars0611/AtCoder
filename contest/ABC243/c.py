import sys
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
sys.setrecursionlimit(10**7)
input = sys.stdin.readline
#----------------------------------------#
import math
import bisect
import itertools
import heapq
from collections import deque
from collections import Counter
from collections import defaultdict
from sortedcontainers import SortedList
from sortedcontainers import SortedSet
from sortedcontainers import SortedDict
from more_itertools import distinct_permutations
from functools import lru_cache
from functools import cmp_to_key
#----------------------------------------#
n = int(input())
pos = [tuple(map(int, input().split())) for _ in range(n)]
s = input().strip()
p = []
t = {'L':0, 'R':1}
for i in range(n):
    p.append((pos[i][0], pos[i][1], t[s[i]]))
p.sort()
flgs = defaultdict(bool)
for i in range(n):
    xi, yi, d = p[i]
    if d == 1:
        flgs[yi] = True
    else:
        if flgs[yi]:
            print("Yes")
            break
else:
    print("No")
