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
s = input().strip()
t = input().strip()
d = []
for i in range(len(s)):
    if ord(t[i]) >= ord(s[i]):
        d.append(ord(t[i]) - ord(s[i]))
    else:
        d.append(ord('z') - ord(s[i]) + ord(t[i]) - ord('a') + 1)
print("Yes" if all(d[i + 1] == d[i] for i in range(len(s) - 1)) else "No")
