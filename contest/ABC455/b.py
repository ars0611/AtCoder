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
ans = 0
for h1 in range(h):
    for h2 in range(h1, h):
        for w1 in range(w):
            for w2 in range(w1, w):
                if all(s[h1 + h2 - i][w1 + w2 - j] == s[i][j] for i in range(h1, h2 + 1) for j in range(w1, w2 + 1)):
                    ans += 1
print(ans)
