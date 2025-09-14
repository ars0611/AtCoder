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
n, k = map(int, input().split())
a = [] #行列入り時刻
b = [] #退店時刻
c = [] #人数
for _ in range(n):
    ai, bi, ci = map(int, input().split())
    a.append(ai)
    b.append(bi)
    c.append(ci)

cnt = 0
time = 0
q = SortedList()
for i in range(n):
    while (q and c[i] + cnt > k) or (q and q[0][0] <= time):
        ctime, ccnt = q.pop(0)
        cnt -= ccnt
        time = max(time, ctime)
    time = max(time, a[i])
    q.add((time + b[i], c[i]))
    cnt += c[i]
    print(time)