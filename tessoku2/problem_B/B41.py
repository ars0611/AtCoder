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
x, y = map(int, input().split())

res = []
while x > 1 or y > 1:
    if not (x, y) == (1, 1):
        res.append((x, y))
    if x >= y:
        x -= y
    else:
        y -= x
    

print(len(res))
while res:
    x, y = res.pop()
    print(x, y)
