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
#----------------------------------------#
n, x, y, z = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
aa = sorted([(a[i], i + 1) for i in range(n)], key=lambda x:(-x[0], x[1]))
bb = sorted([(b[i], i + 1) for i in range(n)], key=lambda x:(-x[0], x[1]))
ss = sorted([(a[i] + b[i], i + 1) for i in range(n)], key=lambda x:(-x[0], x[1]))
p = set()
for i in range(x):
    p.add(aa[i][1])
i = 0
cnt = 0
while cnt != y:
    if bb[i][1] in p:
        i += 1
        continue
    p.add(bb[i][1])
    cnt += 1
    i += 1
i = 0
cnt = 0
while cnt != z:
    if ss[i][1] in p:
        i += 1
        continue
    p.add(ss[i][1])
    cnt += 1
    i += 1
ans = sorted(list(p))
for num in ans:
    print(num, sep="\n")
