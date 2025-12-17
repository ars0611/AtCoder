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
h, m = map(int, input().split())
for _ in range(24 * 60):
    a = h // 10
    b = h % 10
    c = m // 10
    d = m % 10
    if 0 <= a * 10 + c < 24 and 0 <= b * 10 + d < 60:
        print(h, m)
        break
    m += 1
    if m == 60:
        h += 1
        m = 0
    h %= 24
