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
q = list(map(int, input().split()))
a = list(map(int, input().split()))
b = list(map(int, input().split()))

max_a = 10 ** 6
max_b = 10 ** 6 
for i in range(n):
    if a[i] != 0:
        max_a = min(max_a, q[i] // a[i])
    if b[i] != 0:
        max_b = min(max_b, q[i] // b[i])

ans = 0
for i in range(max_a + 1):
    cnt_b = max_b
    for k in range(n):
        cnt_b = min(cnt_b, (q[k] - a[k] * i) // b[k] if b[k] != 0 else float('inf'))
    ans = max(ans, i + cnt_b)

print(ans)