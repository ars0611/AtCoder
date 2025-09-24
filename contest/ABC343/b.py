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
graph = [list(map(int, input().split())) for _ in range(n)]
for i in range(n):
    ans = []
    for j in range(n):
        if graph[i][j] == 1:
            ans.append(j+1)
    print(*ans)