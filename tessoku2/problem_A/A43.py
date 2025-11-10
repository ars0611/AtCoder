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
n, l = map(int, input().split())

ans = 0
for _ in range(n):
    a, b = input().split()
    a = int(a)
    
    if b == "W":
        ans = max(ans, a)
    else:
        ans = max(ans, l - a)

print(ans)