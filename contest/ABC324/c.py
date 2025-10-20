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
n, t_dash = input().split()
n = int(n)
l_t_dash = len(t_dash)
ans = []
for i in range(n):
    s = input().strip()
    l_s = len(s)

    if l_t_dash == l_s:
        cnt = 0
        for j in range(l_s):
            if t_dash[j] != s[j]:
                cnt += 1
            if cnt > 1: break
        if cnt <= 1:
            ans.append(i + 1)

    if l_t_dash - l_s == 1:
        cnt = 0
        for j in range(l_s):
            if t_dash[j] != s[j - cnt]:
                cnt += 1
            if cnt > 1: break
        if cnt == 1 and t_dash[-1] == s[-1] or cnt == 0:
            ans.append(i + 1)

    if l_s - l_t_dash == 1:
        cnt = 0
        for j in range(l_t_dash):
            if t_dash[j - cnt] != s[j]:
                cnt += 1
            if cnt > 1: break
        if cnt == 0 or cnt == 1 and s[-1] == t_dash[-1]:
            ans.append(i + 1)
print(len(ans))
print(*ans)