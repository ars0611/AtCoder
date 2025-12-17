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
n, q = map(int, input().split())
FF = defaultdict(set)
for _ in range(q):
    t, a, b = map(int, input().split())
    if t == 1:
        FF[a].add(b)
    elif t == 2:
        FF[a].discard(b)
    else:
        print("Yes" if b in FF[a] and a in FF[b] else "No")
