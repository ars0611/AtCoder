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
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
b = [list(map(int, input().split())) for _ in range(n)]

for k in range(4):
    ok = True
    for i in range(n):
        for j in range(n):
            if a[i][j] == 0: continue
            if a[i][j] != b[i][j]:
                ok = False
    if ok:
        print("Yes")
        break
    a = [list(ai)[::-1] for ai in zip(*a)]
else:
    print("No")