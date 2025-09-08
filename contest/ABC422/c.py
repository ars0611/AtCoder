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
t = int(input())
for _ in range(t):
    a, b, c = map(int,input().split())
    if min (a,c) <= b:
        print(min(a, c))
    else:
        print(b + min(min(a - b,c - b),(a + c - 2 * b) // 3))