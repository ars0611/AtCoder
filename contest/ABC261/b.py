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
d = {"W":1, "L":-1, "D":0, "-":0}
n = int(input())
a = [input().strip() for _ in range(n)]
t = [[d[a[i][j]] for i in range(n)] for j in range(n)]
flg = True
for i in range(n):
    for j in range(n):
        if t[i][j] + t[j][i] != 0:
            flg = False
print("correct" if flg else "incorrect")
