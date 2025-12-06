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
n, a, b = map(int, input().split())
s = input().strip()
ans = float("inf")
for i in range(n):
    cst = a * i
    rotated = s[i:] + s[:i]
    for j in range(n // 2):
        if rotated[j] != rotated[n - 1 - j]:
            cst += b
    ans = min(ans, cst)
print(ans)
