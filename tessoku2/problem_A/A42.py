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
n, k = map(int, input().split())
players = list(tuple(map(int, input().split())) for _ in range(n))

ans = 0
for min_a in range(1, 101):
    for min_b in range(1, 101):
        cnt = 0
        for ai, bi in players:
            if min_a <= ai <= min_a + k and min_b <= bi <= min_b + k:
                cnt += 1
        ans = max(ans, cnt)

print(ans)