import sys
sys.setrecursionlimit(10**7)
if len(sys.argv) == 2:
    sys.stdin = open(sys.argv[1])
from collections import Counter, deque, defaultdict
from sortedcontainers import SortedSet, SortedList, SortedDict
import heapq, bisect, math, itertools, copy

#----------------------------------------#
n = int(input())
s = [input() for _ in range(n)]
max_len = max(len(s_i) for s_i in s)
ans = [[] for _ in range(max_len)]
ast = [0] * n
for i in range(n-1, 0, -1):
    diff = 0
    for j in range(i-1, -1, -1):
        if len(s[i]) < len(s[j]):
            diff = max(diff, len(s[j]) - len(s[i]))
    ast[i] = diff
for i in range(n-1,-1,-1):
    for j in range(len(s[i])):
        ans[j].append(s[i][j])
        k = 0
    while k < ast[i]:
        ans[len(s[i]) + k].append("*")
        k += 1

for ans_i in ans:
    print("".join(ans_i))