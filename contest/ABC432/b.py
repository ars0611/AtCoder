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
x = list(input().strip())
x.sort()
n = len(x)
m = 9
for i in range(n):
    if x[i] == "0": continue
    m = min(int(x[i]), m)

cmp = False
ans = [f"{m}"]

for i in range(n):
    if not cmp and x[i] == f"{m}":
        cmp = True
        continue
    ans.append(x[i])

print("".join(ans))