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
h, w, n = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(h)]
b = set([int(input()) for _ in range(n)])
ans = 0
for i in range(h):
    cnt = 0
    for j in range(w):
        if a[i][j] in b:
            cnt += 1
    ans = max(ans, cnt)
print(ans)
