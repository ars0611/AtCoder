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
n, q = map(int, input().split())
a = list(map(int, input().split()))
s = [0]
for i in range(n):
    s.append(s[-1] + a[i])
c = 0
for _ in range(q):
    query = list(map(int, input().split()))
    if query[0] == 1:
        c += query[1]
        c %= n
    else:
        l, r = query[1] - 1, query[2] - 1
        r = (r + c) % n + 1
        l = (l + c) % n + 1
        if l < r:
            print(s[r] - s[l - 1])
        elif l == r:
            print(s[r] - s[r - 1])
        else:
            print(s[n] - (s[l - 1] - s[r]))