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
Called = SortedSet()
notCalled = SortedSet(list(i + 1 for i in range(n)))
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0]  == 1:
        p = notCalled.pop(0)
        Called.add(p)
    elif query[0] == 2:
        Called.discard(query[1])
    else:
        print(Called[0])

# あれ、まちがってるはずなのに通ったな。本当はCalledは最初空だよ