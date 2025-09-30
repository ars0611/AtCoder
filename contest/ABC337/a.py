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
n = int(input())
sumx = 0
sumy = 0
for _ in range(n):
    x, y = map(int, input().split())
    sumx += x
    sumy += y
if sumx > sumy:
    print("Takahashi")
elif sumx < sumy:
    print("Aoki")
else:
    print("Draw")