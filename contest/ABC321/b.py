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
n, x = map(int, input().split())
a = list(map(int, input().split()))
score = sum(a) - min(a) - max(a)
a_max = max(a)
a_min = min(a)

diff = x - score
if diff > a_max:
    print(-1)
elif a_max >= diff > a_min:
    print(diff)
else:
    print(0)