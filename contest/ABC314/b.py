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
p = []
b = []
for _ in range(n):
    c = int(input())
    a = set(map(int, input().split()))
    p.append(c)
    b.append(a)

x = int(input())
m = max(p) + 1
ans = []
for i in range(n):
    if x in b[i]:
        if m > p[i]:
            ans = [i + 1]
            m = p[i]
        elif m == p[i]:
            ans.append(i + 1)

print(len(ans))
print(*ans)