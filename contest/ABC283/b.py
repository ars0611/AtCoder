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
n = int(input())
a = list(map(int, input().split()))
q = int(input())
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        a[query[1] - 1] = query[2]
    else:
        print(a[query[1] - 1])
