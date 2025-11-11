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
q = int(input())
heap = []
heapq.heapify(heap)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        heapq.heappush(heap, query[1])
    elif query[0] == 2:
        print(heap[0])
    else:
        heapq.heappop(heap)