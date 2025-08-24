import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
from more_itertools import distinct_permutations
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n, m = map(int, input().split())
g = [input() for _ in range(n)]
score = [0] * n
for i in range(m):
    x = []
    y = []
    for j in range(n):
        if g[j][i] == "1":
            x.append(j)
        else:
            y.append(j)
    if len(x) == 0 or len(y) == 0:
        score = [s + 1 for s in score]
    elif len(x) > len(y):
        for k in y:
            score[k] += 1
    elif len(x) < len(y):
        for k in x:
            score[k] += 1
ans = []
for i in range(n):
    if score[i] == max(score):
        ans.append(i + 1)

print(*ans)