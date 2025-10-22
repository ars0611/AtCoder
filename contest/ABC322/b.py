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
n, m = map(int, input().split())
s = input().strip()
t = input().strip()
if t[:n] == s and t[m - n:m] == s:
    print(0)
elif t[:n] == s:
    print(1)
elif t[m - n:m] == s:
    print(2)
else:
    print(3)