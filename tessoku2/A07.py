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
d = int(input())
n = int(input())
s = [0] * (d + 1)
for _ in range(n):
    l, r = map(int, input().split())
    s[l - 1] += 1
    s[r] -= 1
for i in range(1 , d + 1):
    s[i] = s[i-1] + s[i]
for i in range(d):
    print(s[i])