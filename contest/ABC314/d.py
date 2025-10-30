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
s = list(input().strip())
q = int(input())

safe_upper = set()
safe_lower = set()
u = True
l = True

for i in range(n):
    if s[i].isupper():
        safe_upper.add(i)
    else:
        safe_lower.add(i)

for _ in range(q):
    t, x, c = input().split()
    idx = int(x) - 1
    cmp = c.isupper()

    if t == "1":
        s[idx] = c
        if cmp:
            safe_upper.add(idx)
        else:
            safe_lower.add(idx)

    if t == "2":
        safe_upper.clear()
        u = False
        if not l:
            l = True

    if t == "3":
        safe_lower.clear()
        l = False
        if not u:
            u = True

for i in range(n):
    if s[i].isupper():
        if i in safe_upper or u: continue
        s[i] = s[i].lower()
    else:
        if i in safe_lower or l: continue
        s[i] = s[i].upper()

print("".join(s))