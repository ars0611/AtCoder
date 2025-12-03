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
n, m = map(int, input().split())
graph = [[] for _ in range(n)]
for _ in range(m):
    a, b = map(int ,input().split())
    graph[a - 1].append(b)
    graph[b - 1].append(a)

for i in range(n):
    graph[i].sort()
    res = [f"{node}" for node in graph[i]]
    print(f"{i + 1}:", "{" + ", ".join(res) + "}")
