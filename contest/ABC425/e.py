import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
input = sys.stdin.readline
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools
t, m = map(int, input().split())
for _ in range(t):
    n = int(input())
    c = list(map(int, input().split()))
    l = 0
    d = 1
    for i in range(n):
        l += c[i]
        d *= math.factorial(c[i])
    res = math.factorial(l)
    print(res // d % m)