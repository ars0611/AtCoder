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
h, w = map(int, input().split())
grid = [list(map(int, input().split())) for _ in range(h)]

ans = 0
for bit in range(1 << (h - 1 + w - 1)):
    curi = 0
    curj = 0
    nums = set([grid[curi][curj]])
    for i in range(h - 1 + w - 1):
        if bit & (1 << i):
            curi += 1
        else:
            curj += 1
        if not (0 <= curi < h and 0 <= curj < w): break
        nums.add(grid[curi][curj])
    else:
        if len(nums) == h - 1 + w:
            ans += 1

print(ans)