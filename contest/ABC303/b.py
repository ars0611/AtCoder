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
n, m = map(int, input().split())
a = [list(map(int, input().split())) for _ in range(m)]

fri = [set() for _ in range(n)]
for i in range(m):
    for j in range(n):
        if j == 0:
            fri[a[i][j] - 1].add(a[i][j + 1] - 1)
        elif j == n - 1:
            fri[a[i][j] - 1].add(a[i][j - 1] - 1)
        else:
            fri[a[i][j] - 1].add(a[i][j - 1] - 1)
            fri[a[i][j] - 1].add(a[i][j + 1] - 1)

cnt = 0
for i in range(n):
    cnt += n - len(fri[i]) - 1
print(cnt // 2)