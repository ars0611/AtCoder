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
n, x = map(int, input().split())
x -= 1
a = list(input().strip())

q = deque([x])
a[x] = "@"
while q:
    pos = q.popleft()
    if 0 <= pos - 1 and a[pos - 1] == ".":
        a[pos - 1] = "@"
        q.append(pos - 1)
    if pos + 1 < n and a[pos + 1] == ".":
        a[pos + 1] = "@"
        q.append(pos + 1)

print("".join(a))