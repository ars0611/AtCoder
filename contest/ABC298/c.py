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
q = int(input())
box = defaultdict(SortedList)
num = defaultdict(SortedSet)
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        box[query[2] - 1].add(query[1])
        num[query[1]].add(query[2])
    elif query[0] == 2:
        print(*box[query[1] - 1])
    else:
        print(*num[query[1]])