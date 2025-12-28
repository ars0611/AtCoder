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
a, b = map(int, input().split())
s = str(b / a)
if len(s) > 5:
    if int(s[5]) > 4:
        ans = s[:4] + str(int(s[4]) + 1)
    else:
        ans = s[:5]
else:
    ans = s + "0" * (5 - len(s))
print(ans)
