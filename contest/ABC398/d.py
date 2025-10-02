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
n, r, c = map(int, input().split())
s = input().strip()
fx = 0
fy = 0
dx = [0, 1, 0, -1]
dy = [1, 0, -1, 0]
ans = ""
ng = set([(fx, fy)])
for i in range(n):
    if s[i] == "N":
        kx = dx[0]
        ky = dy[0]
    elif s[i] == "W":
        kx = dx[1]
        ky = dy[1]
    elif s[i] == "S":
        kx = dx[2]
        ky = dy[2]
    else:
        kx = dx[3]
        ky = dy[3]

    r += ky
    c += kx
    fx += kx
    fy += ky
    ng.add((fy, fx))
    if (r,c) in ng:
        ans += "1"
    else:
        ans += "0"
print(ng)
print(ans)