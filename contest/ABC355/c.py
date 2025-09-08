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
n, t = map(int, input().split())
a = list(map(int, input().split()))
h = [0] * n
w = [0] * n
d = [0] * 2
for i,ai in enumerate(a): 
    ai -= 1
    h[ai // n] += 1
    w[ai % n] += 1
    if ai // n == ai % n:
        d[0] += 1
    if ai // n == n - 1 - ai % n:
        d[1] += 1
    if h[ai // n] == n or w[ai % n] == n or d[0] == n or d[1] == n:
        print(i+1)
        exit()

print(-1)