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
n, s, m, l = map(int, input().split())

ans = float("inf")
for i in range(n//6+1, -1, -1):
    for j in range(n//8+1, -1, -1):
        for k in range(n//12+1, -1, -1):
            if i * 6 + j * 8 + k * 12 >= n:
                ans = min(ans, s * i  + m * j + l * k)
print(ans)