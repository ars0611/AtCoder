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
n, m = map(int, input().split())
b = [list(map(int, input().split())) for _ in range(n)]
start = b[0][0]
if 7 - start % 7 < m:
    print("No")
    exit()
for i in range(n):
    for j in range(m):
        if b[i][j] != start + 7 * i + j:
            print("No")
            exit()
print("Yes")
