import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools

#----------------------------------------#
a, b = map(int, input().split())
if a == b:
    ans = -1
else:
    if 1 not in set([a,b]):
        ans = 1
    elif 2 not in set([a,b]):
        ans = 2
    else:
        ans = 3
print(ans)