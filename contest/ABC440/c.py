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
t = int(input())
for _ in range(t):
    n, w = map(int, input().split())
    c = list(map(int, input().split()))
    s = [[0] for _ in range((n - 1) // (2 * w) + 1)]
    for k in range(2):
        for i in range(n):
            s[i // (2 * w)].append(s[i // (2 * w)][-1] + c[i])
        while len(s[-1]) != (k + 1) * (w * 2) + 1:
            s[-1].append(s[-1][-1])
    ans = sum(c)
    for k in range(2 * w):
        cst = 0
        for i in range((n - 1) // (2 * w) + 1):
            cst += s[i][w + k] - s[i][k]
        ans = min(ans, cst)
    print(ans)
    # print(s)
