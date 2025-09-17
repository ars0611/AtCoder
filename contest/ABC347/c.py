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
n, a, b = map(int, input().split())
d = list(map(int, input().split()))

d = list(set(sorted(di % (a+b) for di in d)))

if len(d) == 1:
    print("Yes")
    exit()

max_gap = 0
for i in range(len(d) - 1):
    max_gap = max(max_gap,  d[i+1] - d[i])
max_gap = max(max_gap, (d[0] - d[-1]) % (a + b)) 
print("Yes" if max_gap > b else "No")

# 解説ACすぎる