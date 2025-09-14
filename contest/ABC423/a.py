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
x, c = map(int, input().split())
for i in range(10 ** 7):
    if x - i * 1000 - i * c >= 0:
        continue
    else:
        print((i - 1) * 1000)
        break