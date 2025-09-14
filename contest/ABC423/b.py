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
l = list(map(int, input().split()))
visited = [False] * (n + 1)
visited[0] = True
visited[n] = True
cmp_left = True
cmp_right = True
for i in range(n):
    if cmp_left and l[i] == 0:
        visited[i + 1] = True
    else:
        cmp_left = False
    if cmp_right and l[n - 1 - i] == 0:
        visited[n - 1 - i] = True
    else:
        cmp_right = False

print(n + 1 - sum(visited))