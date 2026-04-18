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
n = int(input())
graph = [[] for _ in range(n)]
for _ in range(n - 1):
    a, b = map(lambda x:int(x) - 1, input().split())
    graph[a].append(b)
    graph[b].append(a)
for i in range(n):
    if len(graph[i]) == n - 1:
        print("Yes")
        break
else:
    print("No")
