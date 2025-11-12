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
#----------------------------------------#
w, h = map(int, input().split())
n = int(input())
pos = list(tuple(map(int, input().split())) for _ in range(n))
a = int(input())
cut_v = [0] + list(map(int, input().split())) + [w]
b = int(input())
cut_h = [0] + list(map(int, input().split())) + [h]

x = [list() for _ in range(a + 2)]
for p, q in pos:
    idx = bisect.bisect_left(cut_v, p)
    x[idx - 1].append(q)
    if x[idx] == p:
        x[idx].append(q)

area = defaultdict(int)
for i in range(a + 2):
    for j in x[i]:
        idx = bisect.bisect_left(cut_h, j)
        area[i + (a + 2) * (idx - 1)] += 1
        if cut_h[idx] == j:
            area[i + (a + 2) * (idx)] += 1

min_ans = n + 1
max_ans = -1
key_cnt = 0
for v in area.values():
    min_ans = min(min_ans, v)
    max_ans = max(max_ans, v)
    key_cnt += 1

if key_cnt < (a + 1) * (b + 1):
    min_ans = 0

print(min_ans, max_ans)