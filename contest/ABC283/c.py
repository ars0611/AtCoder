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
s = input().strip()
n = len(s)
cnt = 0
i = 0
while i < n:
    cnt += 1
    if i + 1 < n and s[i] + s[i + 1] == "00":
        i += 2
    else:
        i += 1
print(cnt)
