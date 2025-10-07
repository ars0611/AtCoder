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
t = int(input())
for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    pos = [[] for __ in range(n)]
    for i in range(2 * n):
        pos[a[i] - 1].append(i)
    cnt = 0
    cnted_pair = set()
    for j in range(2*n - 1):
        if a[j] == a[j + 1]:
            continue
        A = a[j] - 1
        B = a[j + 1] - 1
        if abs(pos[A][0] - pos[A][1]) == 1 or abs(pos[B][0] - pos[B][1]) == 1:
            continue
        q = sorted(pos[A] + pos[B])
        if q[0] + 1 == q[1] and q[2] + 1 == q[3] and (A, B) not in cnted_pair and (B, A) not in cnted_pair:
            cnted_pair.add((A, B))
            cnted_pair.add((B, A))
            cnt += 1
    print(cnt)