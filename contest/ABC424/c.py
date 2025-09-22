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
graph = [[] for _ in range(n)]
skill = set()
queue = deque()
for i in range(n):
    a, b = map(int, input().split())
    if a == 0 and b == 0:
        queue.append(i)
    else:
        graph[a-1].append(i)
        graph[b-1].append(i)

while queue:
    v = queue.popleft()
    if v in skill:
        continue
    skill.add(v)
    for nv in graph[v]:
        if nv not in skill:
            queue.append(nv)

print(len(skill))