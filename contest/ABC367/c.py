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
n, k = map(int, input().split())
r = list(map(int, input().split()))
s = []
for r_i in r:
    s.append(range(1,r_i+1))

#高々5**8パターンしかないので全探索で間に合う
#樹形図全列挙する感覚
for s_i in itertools.product(*s):
    if sum(s_i) % k == 0:
        print(*s_i)

#----------------------------------------#
#解説より,再起関数による実装
a = [0] * n
def solve(lv):
    if lv == n:
        if sum(a) % k == 0:
            print(*a)
        return
    for i in range(1, r[lv]+1):
        a[lv] = i
        solve(lv+1)
solve(0)