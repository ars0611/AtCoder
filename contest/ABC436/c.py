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
plased = set()
cnt = 0
for _ in range(m):
    r, c = map(int, input().split())
    cube = [(r, c), (r, c + 1), (r + 1, c), (r + 1, c + 1)]
    if all(pair not in plased for pair in cube):
        cnt += 1
        for pair in cube:
            plased.add(pair)
print(cnt)
