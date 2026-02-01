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
h, w = map(int, input().split())
s = [input().strip() for _ in range(h)]
tokens = []
for i in range(h):
    for j in range(w):
        if s[i][j] == 'o':
            tokens.append((i, j))
print(abs(tokens[0][0] - tokens[1][0]) + abs(tokens[0][1] - tokens[1][1]))
